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
  print("1 - Portfolio Summary")
  print("2 - Look up Stock Price")
  print("3 - Buy Shares")
  print("4 - Sell Shares")

def portfolioSummary():
  with open('portfolio.json') as file:
    portfolio = json.load(file)
  print()
  print("Portfolio Summary")
  print()
  print("Stock Name",'\t',"Bought At",'\t','\t','    ',"Number of Shares",'\t',"Value")
  totalValue = 0
  for index in range(len(portfolio['stockNames'])):
    print(portfolio['stockNames'][index] , '\t','\t', portfolio['stockPrices'][index]," ",portfolio['shareQuantities'][index],'\t','\t','\t','\t',portfolio['stockPrices'][index] * portfolio['shareQuantities'][index])

    totalValue += portfolio['stockPrices'][index] * portfolio['shareQuantities'][index]
    
  print()
  print("Total Portfolio Value:",totalValue)

def main():
  mainMenu()
  menuOpt = input()

  if menuOpt == '1':
    portfolioSummary()
  if menuOpt == '2':
    print("2")
  if menuOpt == '3':
    print("3")
  if menuOpt == '4':
    print("4")

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
