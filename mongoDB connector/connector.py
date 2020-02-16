# Uses pyMongo to extract data from mongoDB

import pymongo as pm

connection = pm.MongoClient('mongodb+srv://lukemarushack:gHmKkInrZNQeI3B6@economeme-0ffr6.mongodb.net/test?retryWrites=true&w=majority', 27017)
db = connection.Economeme

data = db.memes
friendsList = data.find()

fullSet = {}
for item in friendsList:
    fullSet[item['Meme']] = item['Freq']

def returnData():
    return fullSet

returnData()


