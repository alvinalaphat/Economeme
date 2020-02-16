import matplotlib.pyplot as plt

data = open("memeData.txt", 'r')

def generatePlot(meme):
    plotted = data[meme]
    pastSevenVals = plotted[-7:-1]
    pastWeek = range(1,7)
    plt.plot(pastWeek, pastSevenVals)
    plt.xlabel('Current Trend')
    plt.ylabel('Estimated Impressions')
    plt.title(meme + ' frequency over the past week')

generatePlot('Doge')