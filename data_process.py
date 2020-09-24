from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from urllib.request import Request, urlopen
from tweepy import Stream
import tweepy
import twitter_credentials
import requests
import pymongo as pm
from bs4 import BeautifulSoup
import random

connection = pm.MongoClient('mongodb+srv://lukemarushack:gHmKkInrZNQeI3B6@economeme-0ffr6.mongodb.net/test?retryWrites=true&w=majority', 27017)
db = connection.Economeme
collection = db.memes

def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    
    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    mapper = {}
    count = 0
    for tweet in tweepy.Cursor(api.search, q=hashtag+' -filter:retweets', lang="en", tweet_mode='extended').items():
        count += 1

    if '.' in hashtag:
        hashtag.remove('.')

    if '\'' in hashtag:
        hashtag.remove('\'')

    if 'meme' in dir(collection):
        db.runCommand({
            update: collection,
            updates: [{
                'freq': mapper['freq'].append(count + random.randint(-(int(mapper['freq']*.1)),(int(mapper['freq']*.1))))
            }]
        })
    else:
        mapper['meme'] = hashtag
        mapper['freq'] = [count]
        collection.insert_one(mapper)
    

if __name__ == "__main__":
    memes = []
    for batch in range(1,50):
        site = "https://knowyourmeme.com/categories/meme/page/" + str(batch)
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(site,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, features='html.parser')
        
        for item in soup.select('h2 a'):
            meme = ''.join(item.text.split())
            memes.append(meme)

    for hashtag in memes:
        search_for_hashtags(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET, twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET, hashtag)