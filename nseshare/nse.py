import nselib
from nselib import capital_market
nselib.trading_holiday_calendar()
result = capital_market.bhav_copy_equities('23-09-2024')
print(result)
result1 = capital_market.block_deals_data(period='1M')
print(result1)
result2 = capital_market.bulk_deal_data(period='1M')
print(result2)
result3 = capital_market.deliverable_position_data('SBIN',period='1M')
print(result3)
result4 = capital_market.price_volume_and_deliverable_position_data('INFY',period='1M')
print(result4)
result5 = capital_market.equity_list()
print(result5)


