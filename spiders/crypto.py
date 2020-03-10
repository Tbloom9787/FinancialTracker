import requests
import sys
from bs4 import BeautifulSoup
import csv
import pandas as pd
import requests
import time

API_ENDPOINT = "http://localhost:8000/crypto/"
API_KEY = "b*8p4e%!rk#hzm04$@j@6ie54&*wg+cpmmua0f_-(h4k(qpq0!"
METHOD = "PUT"

# Data Table
id=[]
names=[]
prices=[]
changes=[]
percentChanges=[]

index = 0
url_index = 0

while True:
    # URL to scrape data from
    CryptoUrl = "https://finance.yahoo.com/cryptocurrencies?count=100&offset=" + str(url_index)

    # Send a GET request to retrieve html
    r = requests.get(CryptoUrl)
    data = r.text

    # Load the data into soup
    soup = BeautifulSoup(data, 'lxml')

    # For Loop - Yahoo Finance requires us to crawl through specific
    # attributes to find data
    for listing in soup.find_all('tr', attrs={'class':'simpTblRow'}):
        for name in listing.find_all('td', attrs={'aria-label':'Symbol'}):
            names.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label':'Price (Intraday)'}):
            prices.append(price.text.replace(',', ''))
        for change in listing.find_all('td', attrs={'aria-label':'Change'}):
            changes.append(change.text)
        for percentChange in listing.find_all('td', attrs={'aria-label':'% Change'}):
            percentChanges.append(percentChange.text.replace('%', ''))
        id.append(index)
        index += 1

    data = {
        "id": id,
        "ticker": names,
        "price": prices,
        "change": changes,
        "percentChange": percentChanges
    }

    if url_index != 100:
        url_index += 100
    else:
        if METHOD == "POST":
            requests.post(url=API_ENDPOINT, data={"id": data["id"], "ticker": data["ticker"], "price": data["price"], "change": data["change"], "percentChange": data["percentChange"]})
            sys.exit()

        requests.put(url=API_ENDPOINT, data={"id": data["id"], "ticker": data["ticker"], "price": data["price"], "change": data["change"], "percentChange": data["percentChange"]})
        url_index = 0
        index = 0
        time.sleep(60)