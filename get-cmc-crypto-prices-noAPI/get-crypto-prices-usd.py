# This program scapes the current cryptocurrency price for defined currencies from CMC without the use of the CMC Developer API - therefore avoiding API restrictions
# The following libraries are required:
# Requests, BeautifulSoup4

import time
import requests
from bs4 import BeautifulSoup

currency = ['bitcoin', 'ethereum', 'dogecoin', 'tether']

def parse_page(currency):
    page = requests.get('https://coinmarketcap.com/currencies/' + currency)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def find_price(soup):
    price = soup.find(class_='priceValue___11gHJ').get_text()
    return price

for x in currency:
    #print ('Parsing information for '+ x +'...')
    soup = parse_page(x)
    #print ("Finding Price for " + x + "...")
    price = find_price(soup)
    #print ('Current Price for '+ x + ' is:')
    print ('----------------')
    print ('-----' + x + '-----')
    print ('----------------')
    print (price)
    print ()
