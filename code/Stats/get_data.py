import pandas as pd
import json
from datetime import datetime, timedelta
import numpy as np


import asyncio
import websockets
import json
import pickle
# timestamps 3 years back

now = datetime.now()

now_take_3 = now - timedelta(days=3*365)
now_take_2 = now - timedelta(days=2*365)
now_take_1 = now - timedelta(days=1*365)

now_timestamp = datetime.timestamp(now)*1000
now_take_3_timestamp = datetime.timestamp(now_take_3)*1000
now_take_2_timestamp = datetime.timestamp(now_take_2)*1000
now_take_1_timestamp = datetime.timestamp(now_take_1)*1000

print(f"The current time {now}")
print(f"The 3 years ago  {now_take_3}")
print(f"The 3 years ago  {now_take_2}")
print(f"The 3 years ago  {now_take_1}")

print("_________________________________")
print(f"The current time time stamp (ms) {now_timestamp}")
print(f"The 3 years ago time stamp (ms)  {now_take_3_timestamp}")
print(f"The 3 years ago time stamp (ms)  {now_take_2_timestamp}")
print(f"The 3 years ago time stamp (ms)  {now_take_1_timestamp}")


# msg = \
# {
#   "jsonrpc" : "2.0",
#   "id" : 833,
#   "method" : "public/get_tradingview_chart_data",
#   "params" : {
#     "instrument_name" : "ETH-PERPETUAL",
#     "start_timestamp" : int(now_take_2_timestamp),
#     "end_timestamp" : int(now_take_1_timestamp),
#     "resolution" : "1D"
#   }
# }



msg = \
{
  "jsonrpc" : "2.0",
  "id" : 833,
  "method" : "public/get_tradingview_chart_data",
  "params" : {
    "instrument_name" : "ETH-PERPETUAL",
    "start_timestamp" : int(now_take_1_timestamp),
    "end_timestamp" : int(now_timestamp),
    "resolution" : "1D"
  }
}


async def call_api(msg):
   async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
       await websocket.send(msg)
       while websocket.open:
           response = await websocket.recv()
           # do something with the response...
          #  print(response)
           return response

loop =  asyncio.get_event_loop()
task = loop.create_task(call_api(json.dumps(msg)))
data = loop.run_until_complete(task)

with open("daily_eth.pickle_3","wb") as f:
  pickle.dump(data,f)
