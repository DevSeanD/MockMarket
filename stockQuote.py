"""
Author: Sean Dever
Description: The purpose of this file is to serve as a starting point for the overall mock stock exchange project. It will ask the user for a stock and using the yahoo finance api it will rectrieve the current price.
File Name: stockQuote.py
Dependancies: 
  pip install requests_html
  pip install yfinance
  pip install yahoo_fin
"""

import yfinance
import yahoo_fin.stock_info as si


while(True):
    targetStock = input("What stock would you like to quote? ")

    print(si.get_live_price(targetStock))
    print("")
