"""
Author: Sean Dever
Date: 3/27/2020
Description: A implementation of the iterator design pattern applied to Mock Market. The native language of Mock Market will be python therefore implementing a core function in python is a more sound design choice.
"""

import yfinance
import yahoo_fin.stock_info as si
import math


class UsrStock:
    def __init__(self,name,currentVal,quantity):
        self.name = name
        self.currentVal = currentVal
        self.quantity = quantity

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


currentUsrPortfolio = [] # User stock portfolio collection

# Adding stock to portfolio collection
currentVal = round_up(si.get_live_price("AAPL"),2)
currentUsrPortfolio.append(UsrStock("AAPL",currentVal,5))

currentVal = round_up(si.get_live_price("IBM"),2)
currentUsrPortfolio.append(UsrStock("IBM ",currentVal,6))

currentVal = round_up(si.get_live_price("QCOM"),2)
currentUsrPortfolio.append(UsrStock("QCOM",currentVal,10))

print("\n Current Stock Portfolio")	
portfolioValue = 0

for stock in currentUsrPortfolio:
    print("Name: ",stock.name," Current Price: ",stock.currentVal,"  Quantity Owned: ",stock.quantity)
    portfolioValue += (stock.currentVal * stock.quantity)

print("Total Porfolio Value: ", portfolioValue)

