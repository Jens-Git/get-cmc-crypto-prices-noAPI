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

def find_price_change(soup):
    price_change = soup.find(class_='sc-1v2ivon-0').get_text()
    return price_change

def get_rank(soup):
    rank = soup.find(class_='namePill___3p_Ii namePillPrimary___2-GWA').get_text()
    return rank


for x in currency:
    #print ('Parsing information for '+ x +'...')
    soup = parse_page(x)
    #print ("Finding Price for " + x + "...")
    price = find_price(soup)
    price_change = find_price_change(soup)
    #print ('Current Price for '+ x + ' is:')
    rank = get_rank(soup)

    print ('----------------')
    print ('Currency: ' +x)
    print ('Currently at: ' +rank)
    print ('Price: ' +price)
    print ('24h Change: ' +price_change)
    print ('----------------')
    print ()
