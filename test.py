from pathlib import Path
import csv
import requests

api_key = "demo"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_symbol=USD&to_symbol=SGD&apikey={api_key}"
response = requests.get(url)
currency_exchange_rate = response.json()
