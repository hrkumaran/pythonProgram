import pandas as pd
from datetime import date, timedelta
import numpy as np
from nselib import capital_market
from zoneinfo import ZoneInfo
name_to_index = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
index_to_name = {v: k for k, v in name_to_index.items()}
read_file = pd.read_excel("stocks.xlsx")
float_column = read_file['TargetPrice']  # Replace 'ColumnName' with the actual column name
current_date = date.today()
day = current_date.weekday()
print(day)
if day == 0:
    counterday = 3
    print(counterday)
elif day == 5:
    counterday = 1
    print(counterday)
else:
    counterday = 1
    print(counterday)
yesterday = current_date - timedelta(days=counterday)
print(yesterday)
today = current_date.strftime("%d-%m-%Y");
yesday  = yesterday.strftime("%d-%m-%Y");
print(yesday)
list_of_stock = read_file.to_dict(orient='records')

result = capital_market.week_52_high_low_report(today)
#print(result.columns.values)
print(day,current_date,index_to_name.get(day, day))
print(counterday,yesterday,index_to_name.get(counterday, counterday))
data = capital_market.var_end_of_day(trade_date=yesday)
#print(data.columns.values)
for stock in list_of_stock:
    data = stock['Stock name']
    targetPrice = float(str(stock['TargetPrice']))
    result = capital_market.price_volume_data(data, period='1D')
    closedPriceString = np.array2string(result['ClosePrice'].values)
    if closedPriceString=='':
        print('no valid close price', targetPrice, False)
        continue
    # 1. Remove the square brackets and single quotes
    cleaned_string = closedPriceString.strip("['']")

    # 2. Remove the comma
    cleaned_string = cleaned_string.replace(",", "")

    # 3. Convert the cleaned string to a float
    closedPriceFloat = float(cleaned_string)
    #closedPriceString = result['ClosePrice'].replace(',', '')
    #closedPrice =float(closedPriceString)
    verdict = "Buy" if closedPriceFloat <= targetPrice else "No Buy"
    print(data, index_to_name.get(counterday, counterday), closedPriceFloat, index_to_name.get(day, day), targetPrice, verdict)
    #print(data,closedPriceFloat,targetPrice,(closedPriceFloat<=targetPrice?"Buy":"No Buy"))