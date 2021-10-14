"""
the current price.
File Name: MockMarketCLI.py
Dependencies:
  pip install yfinance
  pip install yahoo_fin

TODO:
  PortfolioSummary - Calculate new value instead of bought at value
  BuyShares function
  SellShares function
  Round sto
Description: The purpose of this file is to serve as a starting point for the overall mock stock market project. It will ask the user for a stock and using the yahoo finance api it will rectrieve the current price.ck price values
"""

import json
import yahoo_fin.stock_info as si
import PythonTableModule


def initialUserSetup():
	# The goal of this function is to prepare the .json file
	# As well as allocate the user some funds to begin with
  print("Hello, and Welcome to MockMarket!")
  print()
  print("The goal of MockMarket is to allow you to gain real world stock experience and knowledge without the risk of capital")
  print()
  validInput = False
  while(validInput == False):
    userCapital = input("How much captial would you like to start with? : $ ",)
    if userCapital.isdigit():
      validInput = True
      
  return userCapital


def mainMenu(userCapitalVal):
	userCaptial = userCapitalVal
	print("=========")
	print("Main Menu")
	print("=========")
	print()
	print("Captial: $" + str(userCaptial))
	print()
	print("1 - Portfolio Summary")
	print("2 - Look up Stock Prices")
	print("3 - Buy Shares")
	print("4 - Sell Shares")


def portfolioSummary():
	with open('portfolio.json') as file:
		portfolio = json.load(file)

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
    
	else:
		print("There are no stocks in your portfolio")
		print()

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

def sellShares(userCaptialVal):
  userCaptial = userCaptialVal
  portfolioSummary()

  tickerToBeSold = input("Enter the ticker of the stock you would like to sell: ")

  with open('portfolio.json') as file:
    portfolio = json.load(file)

  shareTotal = 0
  for index in range(len(portfolio['stockNames'])):
    if portfolio['stockNames'][index] == tickerToBeSold.upper():
      shareTotal += int(portfolio['shareQuantities'][index])
    
  print("You have {} shares of {}".format(shareTotal,tickerToBeSold.upper()))

  if(shareTotal != 0):
    invalidInput = True
    while(invalidInput):
      print("Would you like to sell any?")
      print("1 - Yes")
      print("2 - No")
      choice = input()

      if choice == '1' or choice == '2':
        invalidInput = False
  


def main():
	appLoop = True

	userCaptial = initialUserSetup()

	while (appLoop):
		mainMenu(userCaptial)
		menuOpt = input()

		if menuOpt == '1':
			portfolioSummary()
			print("Portfolio Summary")
		if menuOpt == '2':
			lookUpStockPrices()
		if menuOpt == '3':
			buyShares()
		if menuOpt == '4':
			sellShares(userCaptial)

if __name__ == "__main__":
	main()
