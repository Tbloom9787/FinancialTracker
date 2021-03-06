import requests
import sys
from bs4 import BeautifulSoup
import csv
import pandas as pd
import requests
import time
import json

API_ENDPOINT = "http://localhost:8000/indices/"
API_KEY = "b*8p4e%!rk#hzm04$@j@6ie54&*wg+cpmmua0f_-(h4k(qpq0!"
METHOD = "POST"

# Data Table
ids = []
names = []
prices = []
changes = []
percentChanges = []
index = 0

# URL to scrape data from
IndicesUrl = "https://finance.yahoo.com/world-indices"

# Send a GET request to retrieve html
r = requests.get(IndicesUrl)
data = r.text

while True:
    # Load the data into soup
    soup = BeautifulSoup(data, 'lxml')

    for name in soup.find_all('td', attrs={'class':'data-col1'}):
        names.append(name.text)
    for price in soup.find_all('td', attrs={'class':'data-col2'}):
        prices.append(price.text.replace(',', ''))
    for change in soup.find_all('td', attrs={'class':'data-col3'}):
        changes.append(change.text.replace(',', ''))
    for percentChange in soup.find_all('td', attrs={'class':'data-col4'}):
        percentChanges.append(percentChange.text.replace(',', ''))
        ids.append(index)
        index += 1
    indices = {
        "id": ids,
        "name": names,
        "price": prices,
        "change": changes,
        "percentChange": percentChanges
    }

    if METHOD == "POST":
        requests.post(url=API_ENDPOINT, data=indices)
        sys.exit()
    elif index == 35:
        index = 0

    requests.put(url=API_ENDPOINT, data={"id": ids, "name": names, "price": prices, "change": changes, "percentChange": percentChanges})

    time.sleep(60)
