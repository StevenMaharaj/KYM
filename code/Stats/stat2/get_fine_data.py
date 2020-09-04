import pandas as pd
import requests
from time import sleep
from datetime import datetime, time, timedelta


def break_data(max_points, start, end):
    dt = end
    starts = []
    ends = []
    while dt > start:
        starts.append((dt - timedelta(minutes=max_points*60)).isoformat())
        ends.append(dt.isoformat())
        dt -= timedelta(minutes=max_points*60)
    starts = starts[::-1]
    ends = ends[::-1]
    return starts, ends


start = datetime(2017, 8, 4, 1, 6, 15)
end = datetime(2020, 8, 4, 1, 6, 15)

starts, ends = break_data(300, start, end)
# print(starts[0], ends[0])
end_point = "https://api.pro.coinbase.com"
product_id = "ETH-USD"
# https://api.pro.coinbase.com/products/ETH-USD/candles?start=2020-08-03T20:06:15&end=2020-08-04T01:06:15&granularity=60
data = []
n = len(starts)
for i in range(n):
    print(f"{i}/ {n} done")
    s = starts[i]
    e = ends[i]
    r = requests.get(
    f'{end_point}/products/{product_id}/candles?start={s}&end={e}&granularity=3600')
# print(f'{end_point}/products/{product_id}/candles?start={s}&end={e}granularity=60')
    data += r.json()
    sleep(1.05)
df = pd.DataFrame(data,columns=["time","low","high","open","close","volume"])
df["date_time"] = df['time'].apply(lambda x: datetime.fromtimestamp(x))
df["day"] = df["date_time"].apply(lambda x: x.weekday())
df.set_index('date_time',inplace=True)
df.sort_values(by=["time"], inplace = True)
df.to_csv("ethusd_fine_3_years.csv")
store = pd.HDFStore('store.h5')
store['df'] = df
print(df.head())