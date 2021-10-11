"""
Author: Sean Dever
Description: The purpose of this file is to serve as a starting point for the overall mock stock market project. It will ask the user for a stock and using the yahoo finance api it will rectrieve the current price.
File Name: MockMarketCLI.py
Dependencies:
  pip install yfinance
  pip install yahoo_fin

TODO:
  PortfolioSummary - Calculate new value instead of bought at value
  BuyShares function
  SellShares function
  Round stock price values
"""

import json
import yahoo_fin.stock_info as si
import PythonTableModule


def initalUserSetup():
	# The goal of this function is to prepare the .json file
	# As well as allocate the user some funds to begin with
	pass


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
	
	headerList = ["Stock Name","Bought At","Number of Shares","Total Value"]
	valueList = []
	valueCount = 0
    
	for index in range(len(portfolio['stockNames'])):
		valueCount += 1
		valueList.append(portfolio['stockNames'][index])
		valueList.append("$" + str(portfolio['stockPrices'][index]))
		valueList.append(portfolio['shareQuantities'][index])
		valueList.append("$" + str(float(portfolio['stockPrices'][index]) * float(portfolio['shareQuantities'][index])))
	if valueCount > 0:
		PythonTableModule.createAndPrintTable(headerList,valueList)
		print(headerList)
		print(valueList)
	else:
		print("There are no stocks in your portfolio")
		print()
    
"""
	print("Stock Name", '\t', '\t','\t', "Bought At", '\t', '\t','\t',
	      "Number of Shares", '\t', '\t','\t', "Value")

	totalValue = 0
	largeNumTab = False
	largeQuanTab = False

	for index in range(
	    len(portfolio['stockNames'])
	):  # this loop will execute based on the amount of entries in 'stocknames'

		# print out Stock name, Value bought at, Stock Quantity, and calculated value
		stockPrice = str(portfolio['stockPrices'][index])
		stockPrice = stockPrice.split('.')

		try:
			stockPriceDisplay = stockPrice[0] + '.' + stockPrice[1][
			    0] + stockPrice[1][1]

		except:
			try:
				stockPriceDisplay = stockPrice[0] + '.' + stockPrice[1][0] + "0"

			except:
				stockPriceDisplay = stockPrice[0] + '.' + "00"

		stockValue = str(portfolio['stockPrices'][index] *
		                 float(portfolio['shareQuantities'][index]))
		stockValue = stockValue.split('.')

		try:
			stockValueDisplay = stockValue[0] + '.' + stockValue[1][
			    0] + stockValue[1][1]

		except:
			try:
				stockValueDisplay = stockValue[0] + '.' + stockValue[1][0] + "0"

			except:
				stockValueDisplay = stockValue[0] + '.' + "00"

		if float(stockValueDisplay) > 999.99:
			largeNumTab = True
		
		if int(portfolio['shareQuantities'][index]) > 9:
		  pass

		if (largeNumTab):
			print(portfolio['stockNames'][index], '\t', '\t', '\t','\t',
			      stockPriceDisplay, '\t', '\t','\t',
			      portfolio['shareQuantities'][index], '\t', '\t', '\t', '\t','\t',
			      '\t','\t' ,stockValueDisplay)
		else:
			print(portfolio['stockNames'][index], '\t', '\t', '\t','\t',
			      stockPriceDisplay, '\t', '\t','\t',
			      portfolio['shareQuantities'][index], '\t', '\t', '\t', '\t','\t',
			      '\t', '\t',stockValueDisplay)

		largeNumTab = False

		totalValue = str(
		    float(portfolio['shareQuantities'][index]) *
		    portfolio['stockPrices'][index])

	totalValue = totalValue.split('.')
	
	try:
	  totalValueDisplay = totalValue[0] + '.' + totalValue[1][0] + totalValue[1][
	    1]
	except:
	  try:
	    totalValueDisplay = totalValue[0] + '.' + totalValue[1][0] + "0"
	  except:
	    totalValueDisplay = totalValue[0] + '.' + "00"
  

	print()
	print("Total Portfolio Value:", totalValueDisplay)
"""

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

		currPrice = str(currPrice).split('.')

		try:
			currPriceDisplay = currPrice[0] + '.' + currPrice[1][
			    0] + currPrice[1][1]
      
		except:
			try:
				curryPriceDisplay = currPrice[0] + '.' + currPrice[1][0] + "0"

			except:
				currPriceDisplay = currPrice[0] + '.' + "00"

		print("Current price of", targetStock + ":", currPriceDisplay)
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
		currPrice = str(currPrice).split('.')
		currPriceDisplay = currPrice[0] + '.' + currPrice[1][0] + currPrice[1][
		    1]

		print(targetStock, "$" + str(currPriceDisplay))
		print()
		print("1 - Buy", targetStock)
		print("2 - Main Menu")
		choice = input()

		if choice == '1':
			print("How may shares of", targetStock,"would you like to purchase")
			order = input()

			validInput = order.isdigit()
			while(validInput == False):
			  print("How may shares of", targetStock,"would you like to purchase")
			  order = input()
			  validInput = order.isdigit()

			if(validInput):
			  with open('portfolio.json') as file:
  				portfolio = json.load(file)

			  portfolio['stockNames'].append(targetStock)

			  portfolio['stockPrices'].append(float(currPriceDisplay))

			  portfolio['shareQuantities'].append(order)

			  with open('portfolio.json', 'w') as file:
  				json.dump(portfolio, file, indent=4)

			  invalidInput = True
			  while(invalidInput):
  				print()
  				print("Would you like to buy another Stock?")
  				print("1 - Yes")
  				print("2 - No")
  				choice = input()

  				if choice == '1':
  				  invalidInput = False
  				  buyShares()
  				if choice == '2':
  				  invalidInput = False

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
	appLoop = True

	while (appLoop):
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
