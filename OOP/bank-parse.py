import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def usd():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date="
    res = requests.get(url)
    soup = bs(res.text, 'html.parser')
    usd_rate = soup.find('rate').text
    print(f"Актуальный курс доллара к гривне: {usd_rate}")

def eur():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&date="
    res = requests.get(url)
    soup = bs(res.text, 'html.parser')
    usd_rate = soup.find('rate').text
    print(f"Актуальный курс евро к гривне: {usd_rate}")

usd()
eur()