import requests

url = "http://ip-api.com/json/77.88.55.88"
response = requests.get(url)
data = response.json()

print(response)
print(f"Страна: {data['country']}")
