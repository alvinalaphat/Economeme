from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from urllib.request import Request, urlopen
from tweepy import Stream
import twitter_credentials
import requests
from bs4 import BeautifulSoup

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    def get_meme(item):
        meme = ''.join(item.text.split())
        freq = len(stream.filter(track=[meme]))
        return freq

    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)
    for batch in range(1,100):
        site = "https://knowyourmeme.com/categories/meme/page/" + str(batch)
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(site,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, features='html.parser')
        
        for item in soup.select('h2 a'):
            freq = get_meme(item)
            print(freq)
                