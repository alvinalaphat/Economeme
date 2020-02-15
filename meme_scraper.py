import requests
from bs4 import BeautifulSoup
import data_processing
from urllib.request import Request, urlopen

# import pymongo
# from pymongo import MongoClient

for batch in range(1,100):
    site= "https://knowyourmeme.com/categories/meme/page/" + str(batch)
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page)
    for item in soup.select('h2 a'):
        meme = ''.join(item.text.split())
        # data_processing.StdOutListener(hashtag=meme)
        print(meme)