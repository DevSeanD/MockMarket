"""
File Name: MockMarketCLI.py
Dependencies:
  pip install yfinance
  pip install yahoo_fin

TODO:
  Apply if else to the sellShare function

Description: The purpose of this file is to serve as a starting point for the overall mock stock market project. It will ask the user for a stock and using the yahoo finance api it will rectrieve the current price values
"""

import json
import yahoo_fin.stock_info as si
import sys
import PythonTableModule

def initialUserSetup():
	# The goal of this function is to prepare the .json file
	# As well as allocate the user some funds to begin with
	print("Hello, and Welcome to MockMarket!")
	print()
	print(
	    "The goal of MockMarket is to allow you to gain real world stock experience and knowledge without the risk of capital"
	)
	print()
	validInput = False
	while (validInput == False):
		userCapital = input(
		    "How much captial would you like to start with? : $ ", )
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

	headerList = ["Stock Name", "Bought At", "Number of Shares", "Total Value"]
	valueList = []
	valueCount = 0

	for index in range(len(portfolio['stockNames'])):
		valueCount += 1
		valueList.append(portfolio['stockNames'][index])
		valueList.append("$" + str(portfolio['stockPrices'][index]))
		valueList.append(portfolio['shareQuantities'][index])
		valueList.append("$" + str(
		    float(portfolio['stockPrices'][index]) *
		    float(portfolio['shareQuantities'][index])))
	if valueCount > 0:
		PythonTableModule.createAndPrintTable(headerList, valueList)

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
			print("!A non valid ticker has been entered!")
			print()
			lookUpStockPrices()

		try:
			currPrice = str(currPrice).split('.')
		except:
			print("!A non valid ticker has been entered!")
			print()
			lookUpStockPrices()

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


def buyShares(userCapitalVal):
	userCapital = float(userCapitalVal)
	portfolioSummary()

	flag = True

	print("Buy Shares")
	print()
	while (flag):
		targetStock = input("What stock would you like to buy shares of?: ")

		try:
			currPrice = si.get_live_price(targetStock)
			currPrice = str(currPrice).split('.')

			try:
			  currPriceDisplay = currPrice[0] + '.' + currPrice[1][
			    0] + currPrice[1][1]

			except:
			  try:
				  curryPriceDisplay = currPrice[0] + '.' + currPrice[1][0] + "0"

			  except:
				  currPriceDisplay = currPrice[0] + '.' + "00"

			print(targetStock, "$" + str(currPriceDisplay))
			print()
			print("1 - Buy", targetStock)
			print("2 - Main Menu")
			choice = input()

			if choice == '1':
				print("How may shares of", targetStock,
				      "would you like to purchase")
				order = input()

				validInput = order.isdigit()
				while (validInput == False):
					print("How may shares of", targetStock,
					      "would you like to purchase")
					order = input()
					validInput = order.isdigit()

				if userCapital >= int(order) * float(currPriceDisplay) and validInput:
				  userCapital = userCapital - int(order) * float(currPriceDisplay)
				  print(userCapital)

				  with open('portfolio.json') as file:
				    portfolio = json.load(file)

				    portfolio['stockNames'].append(targetStock)

				    portfolio['stockPrices'].append(float(currPriceDisplay))

				    portfolio['shareQuantities'].append(order)
                                 
				  with open('portfolio.json', 'w') as file:
				    json.dump(portfolio, file, indent=4) 

				  invalidInput = True
				  while (invalidInput):
				    print()
				    print("Would you like to buy another Stock?")
				    print("1 - Yes")
				    print("2 - No")
				    choice = input()

				    if choice == '1':
					    invalidInput = False
					    buyShares(str(userCaptial))
				    if choice == '2':
					    invalidInput = False

				elif userCapital < int(order) * float(currPriceDisplay) and validInput:
				  print("You do not have enough capital to purchase this amount of stock")

			if choice == '2':
				main(False,(str(userCapital)))

			else:
				while choice != '1' and choice != '2':
					print("1 - Buy", targetStock)
					print("2 - Main Menu")
					choice = input()

					if choice == '1':
						buyShares(str(userCapital))
					if choice == '2':
						main(False,str(userCapital))
    
		except:
			main(False,str(userCapital))


def sellShares(userCapitalVal):
	shareCount = 0

	with open('portfolio.json') as file:
	  portfolio = json.load(file)

	for entry in portfolio["stockNames"]:
	  shareCount += 1
  
	if shareCount == 0:
	  print("You do not have any shares to sell")
	  mainMenu(userCapitalVal)

	userCapital = float(userCapitalVal)
	portfolioSummary()

	tickerToBeSold = input("Enter the ticker of the stock you would like to sell: ")

	found = False
	shareTotal = 0
	for index in range(len(portfolio['stockNames'])):
		if portfolio['stockNames'][index] == tickerToBeSold.upper():
			shareTotal += int(portfolio['shareQuantities'][index])
			found = True

	while (not found):
		tickerToBeSold = input(
		    "Enter the ticker of the stock you would like to sell: ")

		with open('portfolio.json') as file:
			portfolio = json.load(file)

		shareTotal = 0
		for index in range(len(portfolio['stockNames'])):
			if portfolio['stockNames'][index] == tickerToBeSold.upper():
				shareTotal += int(portfolio['shareQuantities'][index])
				found = True

	print("You have {} shares of {}".format(shareTotal,tickerToBeSold.upper()))

	if (shareTotal != 0):
		invalidInput = True
		while (invalidInput):
			print("Would you like to sell any?")
			print("1 - Yes")
			print("2 - No")
			choice = input()

			if choice == '1' or choice == '2':
				invalidInput = False

	if choice == '1':
		quantityToBeSold = 0
		invalidInput = True

		while (invalidInput):
			quantityToBeSold = input(
			    "How many of your {} shares of {} would you like to sell? : ".
			    format(shareTotal, tickerToBeSold.upper()))

			if quantityToBeSold.isdigit():
			  invalidInput = False
			  currPrice = si.get_live_price(tickerToBeSold)
			  userCapital += float(currPrice) * int(quantityToBeSold)

		foundEntryListIndex = []  
		for index in range(len(portfolio["stockNames"])-1):
			  if portfolio["stockNames"][index] == tickerToBeSold.upper():
			    foundEntryListIndex.append(index)

		for entry in foundEntryListIndex:
			print(shareTotal)
			print(quantityToBeSold)
      #The case where quantity of the stock entry is greater than the quantityToBeSold
			if int(portfolio["shareQuantities"][int(entry)]) > int(quantityToBeSold):
			  portfolio["shareQuantities"][int(entry)] = int(portfolio["shareQuantities"][int(entry)]) - int(quantityToBeSold)

      #The case where quantity of all stock entries combined is greater than the quantityToBeSold
			elif shareTotal >= int(quantityToBeSold):
			  if int(portfolio["shareQuantities"][int(entry)]) < int(quantityToBeSold):
			    shareTotal -= int(portfolio["shareQuantities"][int(entry)])

			    del portfolio["shareQuantities"][int(entry)]
			    del portfolio["stockNames"][int(entry)]
			    del portfolio["stockPrices"][int(entry)]

        #The case where quantity of the stock entry is equal to the quantityToBeSold

			  elif shareTotal == int(quantityToBeSold):
			    print("Here")
			    del portfolio["shareQuantities"][index]
			    del portfolio["stockNames"][index]
			    del portfolio["stockPrices"][index]


		#Write changes to the json file
		with open('portfolio.json', 'w') as file:
			json.dump(portfolio, file, indent=4)

    #The case where quantity of the stock entry is less than the quantityToBeSold
		if shareTotal < int(quantityToBeSold):
			print("You do not have {} shares of {} to sell".format(quantityToBeSold,tickerToBeSold.upper()))

	if choice == '2':
		print()
		mainMenu(userCapital)

	return userCapital

def main(initSetUpVal, userCapitalVal):
	initSetUp = initSetUpVal
	appLoop = True
	userCapital = userCapitalVal

	if(initSetUpVal):
		userCapital = initialUserSetup()
		initSetUp = False

  #The main loop of the application
	while(appLoop):
    #Call the user menu function
		mainMenu(userCapital)
    #Take in the user's selection
		menuOpt = input()

    #Branch based on user's selection
		if menuOpt == '1':
			portfolioSummary()
			print("Portfolio Summary")
		if menuOpt == '2':
			lookUpStockPrices()
		if menuOpt == '3':
			userCapital = buyShares(userCapital)
			print(userCapital)
		if menuOpt == '4':
			userCapital = sellShares(userCapital)


if __name__ == "__main__":
	initSetUp = True
	main(initSetUp, 0)
