#INFY SBIN TATAMOTOR  ITC LT
import nselib
import pandas
from nselib import capital_market

result = capital_market.nifty50_equity_list()
print(result)
list_of_stock = ['AXISBANK', 'TAPARIA', 'AAVAS', 'AADHARHFC', 'NMDC','IDFCFIRSTB']
#for stock in list_of_stock:
#    result = capital_market.price_volume_and_deliverable_position_data(stock, period='1D')
#    print(stock,result)




