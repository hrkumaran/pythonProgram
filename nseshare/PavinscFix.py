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
# python
for stock in list_of_stock:
    ticker = stock.get('Stock name')
    try:
        targetPrice = float(stock.get('TargetPrice'))
    except (TypeError, ValueError):
        print(ticker, 'invalid targetPrice', stock.get('TargetPrice'))
        continue

    result = capital_market.price_volume_data(ticker, period='1D')

    # Validate result and ClosePrice column
    if result is None or result.empty or 'ClosePrice' not in result.columns:
        print(ticker, 'no data', targetPrice, False)
        continue

    # Convert to numeric and drop NaNs, then take the last available close price
    close_series = pd.to_numeric(result['ClosePrice'], errors='coerce').dropna()
    if close_series.empty:
        print(ticker, 'no valid close price', targetPrice, False)
        continue

    closedPriceFloat = float(close_series.iloc[-1])
    print(ticker, closedPriceFloat, targetPrice, closedPriceFloat <= targetPrice)