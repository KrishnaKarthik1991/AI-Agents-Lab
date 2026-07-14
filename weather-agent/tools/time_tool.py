import requests
from datetime import datetime
def get_time():
    return datetime.now().strftime("%I:%M %p")