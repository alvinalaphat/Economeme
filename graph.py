import requests
import pymongo as pm
import pprint
import matplotlib.pyplot as plt


connection = pm.MongoClient('mongodb+srv://alvinalaphat:1uScotvkqjQkM0HV@economeme-0ffr6.mongodb.net/test?retryWrites=true&w=majority', 27017)
db = connection.Economeme
collection = db.memes

days = [1,2,3,4,5]

def graph():
    memes = {}
    for meme in collection.find():
        print(meme['meme'], meme['freq'])
        fig = plt.figure()        
        plt.plot(days,meme['freq'])
        memes[meme['meme']] = meme['freq']
        plt.savefig("./static/images/" + meme['meme'] + ".png")
        plt.clf()
    return memes

        