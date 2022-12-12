"""
    Using OpenWeather to fetch 5 Day / 3 Hour Forecasts = 40 records
    Api-doc: https://openweathermap.org/api
    Author https://wolfpaulus.com
"""

from urllib.request import urlopen
from json import loads, dump

API_KEY = "3437784639d884cb2b76d92eaad9c2f4"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q=Prescott,az,us&units=imperial&mode=json&appid={API_KEY}"

data = loads(urlopen(URL).read())
assert data is not None and type(data) == dict
forecast = data.get("list")
temperatures = [x.get("main") for x in forecast]
with open("data.json", "w") as f:
    dump(forecast, f)
with open("temp.json", "w") as f:
    dump(temperatures, f)
print(f"Fetched {len(temperatures)} records. Here is the 1st:\n{temperatures[0]}")

low = min([x.get("temp_min") for x in temperatures])
for record in temperatures:
    if record.get("temp_min") == low:
        print(f"Lowest temp is {low} on {record.get('dt_txt')}")
        break