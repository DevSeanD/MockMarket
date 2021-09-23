"""
Author: Sean Dever
Description: The purpose of this file is to serve as a starting point for the overall mock stock market project. It will ask the user for a stock and using the yahoo finance api it will rectrieve the current price.
File Name: MockMarketCLI.py
Dependancies: 
  pip install requests_html
  pip install yfinance
  pip install yahoo_fin
"""

import json
import yahoo_fin.stock_info as si


def main():
  portfolio = {}
  
  while (True):
    print()
    targetStock = input("What stock would you like to quote? ")
    
    currPrice = si.get_live_price(targetStock)
    print("Current price of",targetStock + ":",currPrice)
    print("")

    print("Would you like to buy shares of" , targetStock + "?")
    buyOrNot = input("If yes enter Y followed by the number of shares:  ")
    
    if buyOrNot[0] == 'y' or buyOrNot =='Y':
      numOfShares = int(buyOrNot[1:])

    with open('portfolio.json') as file:
      portfolio = json.load(file)
      
    portfolio['stockNames'].append(targetStock)

    portfolio['stockPrices'].append(si.get_live_price(targetStock))
    
    portfolio['shareQuantities'].append(numOfShares)

    with open('portfolio.json', 'w') as file:
      json.dump(portfolio, file, indent=4)

if __name__ == "__main__":
	main()
