import requests
import json
response = requests.get("https://api.github.com")
data = json.loads(response.text)
print(data)
print(data.keys())
print(data['current_user_url'])
