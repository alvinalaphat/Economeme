import matplotlib.pyplot as plt
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

def generatePlot(meme):
    plotted = returnData()[meme]
    pastSevenVals = plotted[-7:-1]
    pastWeek = range(1,7)
    plt.plot(pastWeek, pastSevenVals, color=(127/255,74/255, 1,1))
    plt.xlabel('Current Trend')
    plt.ylabel('Estimated Impressions')
    plt.title('Frequency of the "' + meme + '" meme over the past week')
    plt.show()

imagesDict = {}

for keyName in fullSet:
    imagesDict[keyName] = generatePlot(keyName)

