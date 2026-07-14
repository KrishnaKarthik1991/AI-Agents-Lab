import requests
def get_joke():
    url = f"https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    joke = response.json()
    return f"{joke['setup']}{joke['punchline']}"