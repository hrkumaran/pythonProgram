# python
import pandas as pd
from datetime import date, timedelta
import numpy as np
from nselib import capital_market

read_file = pd.read_excel("stocks.xlsx")
current_date = date.today()
yesterday = current_date - timedelta(days=1)
today_str = current_date.strftime("%d-%m-%Y")
yesday_str = yesterday.strftime("%d-%m-%Y")

list_of_stock = read_file.to_dict(orient="records")

# optional pre-fetch reports (errors are caught so script continues)
try:
    report_52 = capital_market.week_52_high_low_report(today_str)
except Exception:
    report_52 = None

try:
    var_eod = capital_market.var_end_of_day(trade_date=yesday_str)
except Exception:
    var_eod = None

for stock in list_of_stock:
    # tolerant lookup for column name
    stock_name = stock.get("Stock name") or stock.get("Stock_Name") or stock.get("Symbol")
    if not stock_name:
        print("Skipping row with no stock name")
        continue

    try:
        target_price = float(stock.get("TargetPrice"))
    except Exception:
        print(stock_name, "invalid or missing TargetPrice; skipping")
        continue

    try:
        pv = capital_market.price_volume_data(stock_name, period="1D")
        if pv is None or "ClosePrice" not in pv.columns:
            print(stock_name, "no ClosePrice data")
            continue

        # get last non-null close price and convert to float
        close_series = pv["ClosePrice"].dropna()
        if close_series.empty:
            print(stock_name, "no valid ClosePrice values")
            continue

        last_close = float(close_series.iloc[-1])
    except Exception as e:
        print(stock_name, "error fetching price:", e)
        continue

    print(stock_name, last_close, target_price, last_close <= target_price)