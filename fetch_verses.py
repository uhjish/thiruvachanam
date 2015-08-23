import urllib
import requests
import multiprocessing
from tinydb import TinyDB, where
from tinydb.storages import JSONStorage
from bs4 import BeautifulSoup

from booklist import chapterCounts

base_url = "http://www.malayalambible.in/ops.php"



