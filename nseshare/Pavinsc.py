import pandas as pd
from datetime import date, timedelta
import numpy as np
from nselib import capital_market
read_file = pd.read_excel("stocks.xlsx")
float_column = read_file['TargetPrice']  # Replace 'ColumnName' with the actual column name
current_date = date.today()
yesterday = current_date - timedelta(days=1)
today = current_date.strftime("%d-%m-%Y");
yesday  = yesterday.strftime("%d-%m-%Y");

list_of_stock = read_file.to_dict(orient='records')

result = capital_market.week_52_high_low_report(today)
#print(result.columns.values)
data = capital_market.var_end_of_day(trade_date=yesday)
#print(data.columns.values)
for stock in list_of_stock:
    data = stock['Stock name']
    targetPrice = float(str(stock['TargetPrice']))
    result = capital_market.price_volume_data(data, period='1D')
    closedPriceString = float(np.array2string(result['ClosePrice'].values))
    #closedPriceString = result['ClosePrice'].replace(',', '')
    closedPrice =float(closedPriceString)
    print(data,closedPriceString,targetPrice,closedPriceString<=targetPrice)