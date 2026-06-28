import requests
username = input("Enter the username: ")
url = f"https://api.github.com/users/{username}"
response = requests.get(url)
if response.status_code == 200:
    print("User found!")
    data = response.json()
    print(f"User: {data['login']}")
    print(f"Name: {data.get('name', 'N/A')}")
    print(f"Company: {data.get('company', 'N/A')}")
    print(f"Location: {data.get('location', 'N/A')}")
    print(f"Public Repos: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
    print(f"Following: {data['following']}")
