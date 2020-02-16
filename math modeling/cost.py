# this function will deternine exactly how much a user will make off of a bet
import datetime
from numpy import log

numCoins = 1000

def calculateReturn(waitPeriod, percentInc):
    proportion = (1+(1/log(3+waitPeriod)))*(1.5*percentInc + 100)/100
    return proportion

def userBet(virality, coins, waitPeriod, percentInc = 5): # wait period in days
    global numCoins
    if numCoins < coins:
        print('You do not have enough coins to make that bet!')
        return('You do not have enough coins to make that bet!')
    if coins < 10:
        print("You need to bet at least 10 coins!")
        return("You need to bet at least 10 coins!")
    if percentInc < 5:
        print('Percent increase must be greater than five!')
        return('Percent increase must be greater than zero!')
    if waitPeriod < 1: 
        print("The waiting period must be at least one day!")
        return("The waiting period must be at least one day!")
    numCoins -= coins
    revealDate = datetime.datetime.now() + datetime.timedelta(days = waitPeriod)

    def checkBet():
        global numCoins
        currentVirality = 1000
        # change conditions for datetime.datetime.now to ">'  when implementing 
        if (datetime.datetime.now() == revealDate): 
            return("Your guess has not reached maturity yet!")
        if (datetime.datetime.now() != revealDate and currentVirality >= virality*(percentInc+100)/100): 
            numCoins += round(coins*calculateReturn(waitPeriod, percentInc))

    checkBet()

userBet(50, 5, 1, 10)
print(numCoins)
        
