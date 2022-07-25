from pathlib import Path
import csv
import requests

api_key = "0GB2H0EPEH2W014M"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
response = requests.get(url)
currency_exchange_rate = response.json()

exchange_rate = []
for items in currency_exchange_rate:
    exchange_rate.append(currency_exchange_rate[items]['5. Exchange Rate'])
print(exchange_rate)









#profit_and_loss
from pathlib import Path
import csv


empty_list=[]
fp=Path.cwd()/"profit-and-loss-hkd (1).csv"
with fp.open(mode="r",encoding="UTF-8")as file:
    reader=csv.reader(file)
    next(reader)
    for values in reader:
        empty_list.append(values[4])
    for items in empty_list:

