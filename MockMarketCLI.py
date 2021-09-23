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
		targetStock = input("What stock would you like to quote? ")

		print(si.get_live_price(targetStock))
		print("")

		with open('portfolio.json') as file:
			portfolio = json.load(file)

		portfolio['stock_names'].append(targetStock)

		with open('portfolio.json', 'w') as file:
			json.dump(portfolio, file, indent=4)


if __name__ == "__main__":
	main()
