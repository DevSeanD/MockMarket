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

def mainMenu():
  print("=========")
  print("Main Menu")
  print("=========")
  print()
  print()
  print("1 - Poftfolio Summary")
  print("2 -")

def portfolioSummary():
  with open('portfolio.json') as file:
    portfolio = json.load(file)

  print("Stock Name",'\t',"Bought At",'\t','\t','    ',"Number of Shares")
  for index in range(len(portfolio['stockNames'])):
    print(portfolio['stockNames'][index] , '\t','\t', portfolio['stockPrices'][index]," ",portfolio['shareQuantities'][index])

def main():
  
  while (True):
    print()
    targetStock = input("What stock would you like to quote? ")
    
    try:
      currPrice = si.get_live_price(targetStock)
    except:
      print("a Non Valid Ticker has been entered")
      main()
      
    print("Current price of",targetStock + ":",currPrice)
    print("")

    print("Would you like to buy shares of" , targetStock + "?")
    buyOrNot = input("If yes enter the number of shares:  ")
    
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
