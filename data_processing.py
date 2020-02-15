import requests
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool
import flask
from flask import Flask, render_template, request
import pandas as pd
from time import sleep
from random import randint
# import pymongo
# from pymongo import MongoClient
from flask import json
from werkzeug.exceptions import HTTPException
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)

    stream.filter(track=['donald trump'])