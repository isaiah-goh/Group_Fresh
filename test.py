#api call



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

def profitloss_function():
    number_1=-1
    number_2=0       
    difference=[]
    data = ""
    for items in range(0,5):
        number_1+=1
        number_2+=1
        difference.append((int(empty_list[number_2])-int(empty_list[number_1])))
    if min(difference)>0:
        return f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
    for date,subtract in enumerate(difference,37):
        if subtract<0:
            value = subtract* -1
            data += f"[PROFIT DEFICIT] DAY {date}, AMOUNT :SGD{round(float(value)*float(api.exchange_rate[0]),2)}" "\n"
    return data
profitloss_function()
        
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

def coh_function():
    number_1=-1
    number_2=0  
    data = "" 
    difference=[]
    for items in range(0,5):
        number_1+=1
        number_2+=1
        difference.append((int(amount[number_2])-int(amount[number_1])))
    if min(difference)>0:
        return f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY" "\n"
    for date,subtract in enumerate(difference,37):
        if subtract<0:
            value = subtract* -1
            data += f"[CASH DEFICIT] DAY {date}, AMOUNT :SGD{round(float(value)*float(api.exchange_rate[0]),2)}" "\n"          
    return data
coh_function()

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

def overhead_function():
    for i,amount in enumerate(expenses_value):
        if amount == max(expenses_value):
            return f"[HIGHEST OVERHEADS] {expenses_type[i]}: SGD{round(float(amount)*float(api.exchange_rate[0]),2)}"
overhead_function()

#main.py
import api, cash_on_hand, overheads, profit_loss
from pathlib import Path

fp = Path.cwd()/"summary_report.txt"
fp.touch()

with fp.open(mode="w", encoding="UTF-8",) as file:
    file.write(api.api_function())
    file.write("\n")
    file.write(overheads.overhead_function())
    file.write("\n")
    file.write(cash_on_hand.coh_function())
    file.write(profit_loss.profitloss_function())
    
