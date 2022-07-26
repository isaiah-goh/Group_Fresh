#api call
import requests
# import requests module

api_key = "0GB2H0EPEH2W014M"
# get api key

url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
# url that shows the exchange rate between USD and SGD

response = requests.get(url)
# use get method from requests on the api url

currency_exchange_rate = response.json()
# use json method to from request to get data from the website and assign to the variable currency_exchange_rate


exchange_rate = []
# create empty list to append exchange rate inside

def api_function():
    """
    - shows the exchange rate between USD and SGD
    """
    for items in currency_exchange_rate:
    # use for loop to iterate over the items from the extracted data from the website    
        exchange_rate.append(currency_exchange_rate[items]['5. Exchange Rate'])
        # append the exchange rate value into the empty list
    return f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{exchange_rate[0]}"
    # return the statement that needs to be put into the text file
api_function()


#profit_and_loss
from pathlib import Path
import csv, api

 
empty_list=[]
date=[]
#create empty list to append values extracted from the csv files

fp=Path.cwd()/"csv_reports"/"Profits and Loss.csv"
#create file path to access profit and loss csv file downloaded from monsoonsim
 
with fp.open(mode="r",encoding="UTF-8")as file:
    #open the file to read file
    reader=csv.reader(file)
    #create reader object 
     next(reader)
    # skip the header for better mathematical calculations in future steps
     
    for values in reader:
        # use for loop to read csv file
        
        empty_list.append(values[4])
         # use indexing to extract the net profit
        
        date.append(values[0])
        #use indexing to extract the dates 
        
day = int(date[0]) + 1
#create day variable to match the difference in profit later in the code 
def profitloss_function():
    '''
    the profitloss function extracts the difference in net profit 
    this function returns the profit deficit of two consecutive days.
    if there is not profit deficit , function returns net profit on each day is higher than the previous

    '''
    
    number_1=-1
    number_2=0  
    # create two variables so that the days increases with each loop 
         
    difference=[]
    #create empty list to append profit difference between 2 consecutive day
    
    data = ""
    #create empty string to make the statement to a string 
   
    for items in range(0,5):
         #for loop to iterate through empty list 
        
        number_1+=1
        number_2+=1
         #create variables to allow the indexing of numbers to increase accordingly to the number of loops
         
        difference.append((int(empty_list[number_2])-int(empty_list[number_1])))
        #find the difference between the profits of censecutive day
   
    if min(difference)>0:
        return f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
         # use conditionals to return the required requirements accordingly 
    #scenario 1 -- there is no profit deficit
     
    for date,subtract in enumerate(difference,day):
        if subtract<0:
            value = subtract* -1
            data += f"[PROFIT DEFICIT] DAY {date}, AMOUNT :SGD{round(float(value)*float(api.exchange_rate[0]),2)}" "\n"
    return data
profitloss_function()
#scenario 2--- there is profit deficit 
    # create for loop to extract profit deficits 
    #use enumerate to match the dates to the profit deficits accordingly
        
#Cash on Hand
from pathlib import Path
import csv, api

amount = []
date = []
fp = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
#creating of file path to csv
with fp.open(mode ="r", encoding="UTF-8") as x:
    reader=csv.reader(x)
    next(reader)
    for values in reader:
        amount.append(values[1])
        date.append(values[0])
#reading the csv and appending the day and amount values into empty lists
day = int(date[0]) + 1
def coh_function():
    """
    This code is used to compute the difference in Cash-on-Hand between each day.
    """
    number_1=-1
    number_2=0  
    data = "" 
    difference=[]
    for items in range(0,5):
        number_1+=1
        number_2+=1
        difference.append((int(amount[number_2])-int(amount[number_1])))
    #for loop to iterate the amount list and append the difference in each days amount into a empty list
    if min(difference)>0:
        return f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY" "\n"
    #if the smallest difference is less then zero it will produce this output
    for date,subtract in enumerate(difference,day):
        if subtract<0:
            value = subtract* -1
            data += f"[CASH DEFICIT] DAY {date}, AMOUNT :SGD{round(float(value)*float(api.exchange_rate[0]),2)}" "\n" 
     #use enumerate to match the dates to the cash deficits accordingly 
    return data
coh_function()

#OVERHEADS 
from pathlib import Path
import csv, api

expenses_value=[]
#create empty list to append the value for the expense
expenses_type=[]
#create empty list to append the type of expense

fp = Path.cwd()/"csv_reports"/"Overheads.csv"
#locate overheads.csv in the current working directory by creating a file path object

with fp.open(mode="r", encoding="UTF-8") as file:
#open file in read mode
    reader = csv.reader(file)
    #create a csv object
    next(reader)
    # skip header in the csv file
    for values in reader:
    # use for loop to iterate over the data in the overheads.csv
        expenses_type.append(values[0])
        # append the type of expense to the empty list
        expenses_value.append(values[1])
        # append the value of the expense to the empty list

def overhead_function():
    """
    - find out the expense in the overheads that is the highest and its value
    """
    for i,amount in enumerate(expenses_value):
     #use enumerate to match the dates to the overheads accordingly 
        if amount == max(expenses_value):
        # if is created as a condition when the code run to highlight the highest overhead expense
            return f"[HIGHEST OVERHEADS] {expenses_type[i]}: SGD{round(float(amount)*float(api.exchange_rate[0]),2)}"
overhead_function() 

#main.py
import api, cash_on_hand, overheads, profit_loss
# import function  from  api, cash_on_hand, overheads and profit_loss

from pathlib import Path
# Import Path from pathlib

fp = Path.cwd()/"summary_report.txt"
# To locate summary_report.txt in the current working directory by creating a file path object

fp.touch()
# create the text file as it does not exist

with fp.open(mode="w", encoding="UTF-8",) as file:
# Open the file in write mode

    file.write(api.api_function())
    # Write currency rate to text file
    file.write("\n")
    # Write to the next line
    file.write(overheads.overhead_function())
    # Write highest overhead expense and its accompanied value to text file
    file.write("\n")
    # Write to the next line
    file.write(cash_on_hand.coh_function())
    # Write the days that cash in hand that is lower than the previous day and its accompanied value to the text file.
    file.write(profit_loss.profitloss_function())
    # Write the day that has a lower profit than the previous day and its accompanied value to the text file.
    
