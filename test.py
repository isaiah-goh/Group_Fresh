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
date=[]
fp=Path.cwd()/"profit-and-loss-usd.csv"
with fp.open(mode="r",encoding="UTF-8")as file:
    reader=csv.reader(file)
    next(reader)
    for values in reader:
        empty_list.append(values[4])
        date.append(values[0])
print(empty_list)
print(date)
number_1=-1
number_2=0       
difference=[]

for items in range(0,5):
    number_1+=1
    number_2+=1
    difference.append((int(empty_list[number_2])-int(empty_list[number_1])))
print(difference)

