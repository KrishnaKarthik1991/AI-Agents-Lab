import requests
city = input("Enter the city name: ")
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)
data = response.json()
current_condition = data['current_condition'][0]
temperature = current_condition['temp_C']
print(f"The current temperature in {city} is {temperature}°C.") 
print(f"The weather description is: {current_condition['weatherDesc'][0]['value']}.")
print(f"The humidity is: {current_condition['humidity']}%.")
print(f"The wind speed is: {current_condition['windspeedKmph']} km/h.")
print(f"The visibility is: {current_condition['visibility']} km.")
print(f"The pressure is: {current_condition['pressure']} hPa.")
print(f"The cloud cover is: {current_condition['cloudcover']}%.")
print(f"The UV index is: {current_condition['uvIndex']}.")