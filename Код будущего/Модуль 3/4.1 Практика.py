import requests

url = "https://api.agify.io?name=alex"
response = requests.get(url)
data = response.json()

print(data)