#api call
import requests

api_key = "0GB2H0EPEH2W014M"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
response = requests.get(url)
currency_exchange_rate = response.json()


exchange_rate = []
def api_function():
    for items in currency_exchange_rate:
        exchange_rate.append(currency_exchange_rate[items]['5. Exchange Rate'])
    return f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{exchange_rate[0]}"
api_function()


#profit_and_loss
from pathlib import Path
import csv, api


empty_list=[]
date=[]
fp=Path.cwd()/"csv_reports"/"Profits and Loss.csv"
with fp.open(mode="r",encoding="UTF-8")as file:
    reader=csv.reader(file)
    next(reader)
    for values in reader:
        empty_list.append(values[4])
        date.append(values[0])

def profit_and_loss():
    number_1=-1
    number_2=0       
    difference=[]
    for items in range(0,5):
        number_1+=1
        number_2+=1
        difference.append((int(empty_list[number_2])-int(empty_list[number_1])))
    for date,subtract in enumerate(difference,37):
        if subtract<0:
            value = subtract* -1
            print(f"[PROFIT DEFICIT] DAY {date}, AMOUNT :SGD{float(value)*float(api.exchange_rate[0])}")
        else:
            if min(difference)>0:
                print(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
profit_and_loss()
        
#Cash on Hand
from pathlib import Path
import csv, api

amount = []
date = []
fp = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
with fp.open(mode ="r", encoding="UTF-8") as x:
    reader=csv.reader(x)
    next(reader)
    for values in reader:
        amount.append(values[1])
        date.append(values[0])

def coh():
    number_1=-1
    number_2=0       
    difference=[]
    for items in range(0,5):
        number_1+=1
        number_2+=1
        difference.append((int(amount[number_2])-int(amount[number_1])))
    for date,subtract in enumerate(difference,37):
        if subtract<0:
            value = subtract* -1
            print(f"[CASH DEFICIT] DAY {date}, AMOUNT :SGD{round(float(value)*float(api.exchange_rate[0]),2)}")
        else:
            if min(difference)>0:
                print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
coh()

#OVERHEADS 
from pathlib import Path
import csv, api

expenses_value=[]
expenses_type=[]

fp = Path.cwd()/"csv_reports"/"Overheads.csv"

with fp.open(mode="r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    next(reader)
    for values in reader:
        expenses_type.append(values[0])
        expenses_value.append(values[1])

def expense():
    for i,amount in enumerate(expenses_value):
        if amount == max(expenses_value):
            print(f"[HIGHEST OVERHEADS] {expenses_type[i]}: SGD{float(amount)*float(api.exchange_rate[0])}")
expense()

#main.py
import api, coh, overheads, profit_loss
from pathlib import Path

def main():
    forex = api.api_function()
    overheads.overhead_function()
    coh.coh_function()
    profit_loss.profitloss_function()

output = main()

fp = Path.cwd()/"summary_report.txt"
fp.touch()
with fp.open(mode="w", encoding="UTF-8") as file:
    file.write(output)
    
