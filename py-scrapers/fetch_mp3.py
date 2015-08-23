import sys
import os
import urllib
import requests
import multiprocessing
from bs4 import BeautifulSoup


def _reporthook(numblocks, blocksize, filesize, url=None):
    #print "reporthook(%s, %s, %s)" % (numblocks, blocksize, filesize)
    base = os.path.basename(url)
    #XXX Should handle possible filesize=-1.
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
    except:
        percent = 100
    if numblocks != 0:
        sys.stdout.write("\b"*70)
    sys.stdout.write("%-66s%3d%%" % (base, percent))


def geturl(url, dst):
    print "get url '%s' to '%s'" % (url, dst)
    if sys.stdout.isatty():
        urllib.urlretrieve(url, dst,
                           lambda nb, bs, fs, 
                           url=url: _reporthook(nb, bs, fs, url))
        sys.stdout.write('\n')
    else:
        urllib.urlretrieve(url, dst)


def fetch_mp3(mp3):
    (dirpart, fname) = os.path.split(mp3)
    if not os.path.isdir(dirpart):
        os.makedirs(dirpart)
    geturl("%s%s" % (base_url, mp3), mp3)


pl_pfx = "JavaScript:PlayAudio('"
pl_sfx = "');"
base_url = "http://audiobible.keralabiblesociety.com/"
mp3_rels = []


for book_id in xrange(1, 74):
    r = requests.get("http://audiobible.keralabiblesociety.com/biblelist.php",
                     params={"lngId": book_id, "b": "m", "retHTML": 1})
    soup = BeautifulSoup(r.text, 'html.parser')
    mp3_rels += [x.get('onclick').replace(pl_pfx, "").replace(pl_sfx, "")
                 for x in soup.find_all('a')]
    print >>sys.stderr, "Harvesting, %d files, last: %s" % \
        (len(mp3_rels), mp3_rels[-1])

pool = multiprocessing.Pool(4) 
pool.map(fetch_mp3, mp3_rels)

