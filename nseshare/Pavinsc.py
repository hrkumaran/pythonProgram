import pandas as pd
import json
import requests
#INFY SBIN TATAMOTOR  ITC LT
import nselib
from nselib import capital_market
read_file = pd.read_excel("stocks.xlsx")
#list_of_stock = ['INFY', 'SBIN', 'TATAMOTOR', 'ITC', 'LT']
#for stock in read_file[['Stocks']]:
   #result = capital_market.price_volume_and_deliverable_position_data(stock, period='1D')
   #print(stock)

#print(read_file[['Stock name']])

list_of_stock = read_file.to_dict(orient='records')
result = capital_market.week_52_high_low_report('25-09-2024')
#print(result.columns.values)
data = capital_market.var_end_of_day(trade_date='25-09-2024')
#print(data.columns.values)
for stock in list_of_stock:
    data = stock['Stock name']
    targetPrice =
    result = capital_market.price_volume_data(data, period='1D')
    print(data,result['ClosePrice'].values)