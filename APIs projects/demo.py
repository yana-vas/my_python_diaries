import json
import requests as requests

key = "https://api2.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
data = requests.get(key)
data = data.json()
print(f"{data['symbol']} price is {data['price']}")
