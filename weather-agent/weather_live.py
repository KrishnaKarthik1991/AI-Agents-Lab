import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m"
response = requests.get(url)
print(response.text)
import json
data = json.loads(response.text)
print(data.keys())
