import urllib
from tinydb import TinyDB, where
from tinydb.storages import JSONStorage
from bs4 import BeautifulSoup
import gevent.monkey
gevent.monkey.patch_socket()
from gevent.pool import Pool
import requests

from booklist import chapterCounts

base_url = "http://www.malayalambible.in/ops.php"

def check_urls(chapters):
    pass

def process_content(content):
    soup = BeautifulSoup(content,"lxml")
    verses = soup.find_all("td", class_="v_text")
    [s.extract() for s in soup('a')]
    for v in verses:
        print v['ref'], "\n".join([s for s in v.strings])
    pass

def fetch_chapter(book_num, chapter_num):
    ref = str(book_num) + "%3A" + str(chapter_num) + "%3A1"
    response = requests.request('GET', base_url, 
                                cookies={"ref":ref},
                                params={"f":"loadverses"})
    process_content(response.content)

"""
pool = Pool(1)
for bk, chap in enumerate(chapters):
    pool.spawn(fetch_chapter, bk, chap)
pool.join()
"""

chapter_counts = dict(chapterCounts)
booknum_to_name = dict(enumerate(chapter_counts.keys()))

chapters = []

for chap, count in enumerate(chapter_counts.values()):
    chapters += zip([chap+1]*count, range(1,count+1))
print chapters

#check_urls([(3,1,)])
#fetch_chapter(3,1)
#fetch_chapter(7,1)



