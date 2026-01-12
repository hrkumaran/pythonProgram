import pandas as pd
from datetime import date, timedelta
import numpy as np
from nselib import capital_market
from flask import Flask

app = Flask(__name__)

name_to_index = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
index_to_name = {v: k for k, v in name_to_index.items()}
read_file = pd.read_excel("stocks.xlsx")
float_column = read_file['TargetPrice']  # Replace 'ColumnName' with the actual column name
current_date = date.today()
day = current_date.weekday()
# print(day)
if day == 0:
    counterday = 3
#    print(counterday)
elif day == 5:
    counterday = 1
#    print(counterday)
elif day == 6:
    counterday = 2
#    print(counterday)
else:
    counterday = 1
#    print(counterday)
yesterday = current_date - timedelta(days=counterday)
# print(yesterday)
today = current_date.strftime("%d-%m-%Y");
yesday = yesterday.strftime("%d-%m-%Y");
# print(yesday)
list_of_stock = read_file.to_dict(orient='records')

result = capital_market.week_52_high_low_report(today)
# print(result.columns.values)
# print(day,current_date,index_to_name.get(day, day))
# print(counterday,yesterday,index_to_name.get(counterday, counterday))
data = capital_market.var_end_of_day(trade_date=yesday)
# print(data.columns.values)
output_data = []
for stock in list_of_stock:
    data = stock['Stock name']
    targetPrice = float(str(stock['TargetPrice']))
    result = capital_market.price_volume_data(data, period='1D')
    closedPriceString = np.array2string(result['ClosePrice'].values)
    if closedPriceString == '':
        print('no valid close price', targetPrice, False)
        continue
    # 1. Remove the square brackets and single quotes
    cleaned_string = closedPriceString.strip("['']")

    # 2. Remove the comma
    cleaned_string = cleaned_string.replace(",", "").strip()

    # 3. Convert the cleaned string to a float
    try:
        # 3. Convert the cleaned string to a float
        closedPriceFloat = float(cleaned_string)
    except ValueError:
        print(f"Error converting to float: {cleaned_string}")
        continue
    # closedPriceString = result['ClosePrice'].replace(',', '')
    # closedPrice =float(closedPriceString)
    verdict = "Buy" if closedPriceFloat <= targetPrice else "NoBuy"
    output_data.append(
        [data, index_to_name.get(counterday, counterday), closedPriceFloat, index_to_name.get(day, day), targetPrice,
         verdict])
#    print(data, index_to_name.get(counterday, counterday), closedPriceFloat, index_to_name.get(day, day), targetPrice,
 #         verdict)

    output_data.append(
        [data, index_to_name.get(counterday, counterday), closedPriceFloat, index_to_name.get(day, day), targetPrice,
         verdict])

@app.route("/")
def home():
    rows = ""
    for line in output_data.strip().split("\n"):
        parts = line.split()
        stock = parts[0]
        thursday = parts[2]
        monday = parts[4]
        decision = parts[5]

        if decision == "Buy":
            color = "#2ecc71"  # green
            bg = "#eafaf1"
        else:
            color = "#e74c3c"  # red
            bg = "#fdecea"

        rows += f"""
           <tr>
               <td>{stock}</td>
               <td>{thursday}</td>
               <td>{monday}</td>
               <td style="color:{color}; background:{bg}; font-weight:bold; border-radius:5px;">
                   {decision}
               </td>
           </tr>
           """

    return f"""
    <html>
    <head>
        <title>Stock Analysis</title>
        <style>
            body {{ font-family: Arial; padding: 20px; background:#f4f4f4; }}
            table {{ border-collapse: collapse; width: 100%; background:white; }}
            th, td {{ padding: 10px; border: 1px solid #ccc; text-align: center; }}
            th {{ background: #333; color: white; }}
            tr:nth-child(even) {{ background:#f2f2f2; }}
        </style>
    </head>
    <body>
        <h2>Stock Recommendation Table</h2>
        <table>
            <tr>
                <th>Stock</th>
                <th>Thursday Price</th>
                <th>Monday Price</th>
                <th>Recommendation</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
