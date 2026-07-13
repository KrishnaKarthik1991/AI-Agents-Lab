import requests
def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    return response.text
def calculator(expression):
    return str(eval(expression))
from datetime import datetime
def get_time():
    return datetime.now().strftime("%I:%M %p")