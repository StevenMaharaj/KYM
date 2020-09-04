import pandas as pd
import requests

from datetime imoprt datetime

def break_data(max_points,start,end,resolution):

end_point = "https://api.pro.coinbase.com"
product_id = "ETH-USD"
r =  requests.get(f'{end_point}/products/{product-id}/candles')  