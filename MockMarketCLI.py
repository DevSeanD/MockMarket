"""
Author: Sean Dever
Description: The purpose of this file is to serve as a starting point for the overall mock stock market project. It will ask the user for a stock and using the yahoo finance api it will rectrieve the current price.
File Name: MockMarketCLI.py
Dependancies:
  pip install yfinance
  pip install yahoo_fin

TODO:
  BuyShares function
  SellShares function
  Round stock price values
"""

import json
import yahoo_fin.stock_info as si


def mainMenu():
	print("=========")
	print("Main Menu")
	print("=========")
	print()
	print("1 - Portfolio Summary")
	print("2 - Look up Stock Prices")
	print("3 - Buy Shares")
	print("4 - Sell Shares")


def portfolioSummary():
	with open('portfolio.json') as file:
		portfolio = json.load(file)

	print()
	print("Portfolio Summary")
	print()
	print("Stock Name", '\t', "Bought At", '\t', '\t', '    ',
	      "Number of Shares", '\t', "Value")

	totalValue = 0

	for index in range(len(portfolio['stockNames'])):
		print(
		    portfolio['stockNames'][index], '\t', '\t',
		    portfolio['stockPrices'][index], " ",
		    portfolio['shareQuantities'][index], '\t', '\t', '\t', '\t',
		    float(portfolio['stockPrices'][index]) * float(portfolio['shareQuantities'][index]))

		totalValue += float(portfolio['stockPrices'][index]) * float(portfolio[
		    'shareQuantities'][index])

	print()
	print("Total Portfolio Value:", totalValue)


def lookUpStockPrices():
	flag = True

	print("Look Up Stock Prices")
	print()
	while (flag):
		targetStock = input("What stock would you like to quote? ")

		try:
			currPrice = si.get_live_price(targetStock)
		except:
			print("a Non Valid Ticker has been entered")
			mainMenu()

		print("Current price of", targetStock + ":", currPrice)
		print("")
		choice = input("Hit enter to continue or 'quit' to exit")

		if choice == "quit" or choice == "QUIT" or choice == "Quit":
			flag = False


def buyShares():
	flag = True

	print("Buy Shares")
	print()
	while (flag):
		targetStock = input("What stock would you like to buy shares of?: ")

		try:
			currPrice = si.get_live_price(targetStock)
		except:
			print("a Non Valid Ticker has been entered")

		print(targetStock, "$" + str(currPrice))
		print()
		print("1 - Buy", targetStock)
		print("2 - Main Menu")
		choice = input()

		if choice == '1' or choice == '2':
		  validInput = True
		  
		  while(validInput):
			  print("How may shares of", targetStock,
			      "would you like to purchase")
			  order = input()
			  
			  validInput = not order.isdigit()
		  with open('portfolio.json') as file:
			  portfolio = json.load(file)

		  portfolio['stockNames'].append(targetStock)

		  portfolio['stockPrices'].append(currPrice)

		  portfolio['shareQuantities'].append(order)

		  with open('portfolio.json', 'w') as file:
		    json.dump(portfolio, file, indent=4)

		if choice == '2':
			main()

		else:
			while choice != '1' and choice != '2':
				print("1 - Buy", targetStock)
				print("2 - Main Menu")
				choice = input()

				if choice == '1':
				  buyShares()
				if choice == '2':
					main()


def main():
	mainMenu()
	menuOpt = input()

	if menuOpt == '1':
		portfolioSummary()
	if menuOpt == '2':
		lookUpStockPrices()
	if menuOpt == '3':
		buyShares()
	if menuOpt == '4':
		print("4")

if __name__ == "__main__":
	main()
