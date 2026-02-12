import requests

url = "https://api.ipify.org?format=json"
response = requests.get(url)
data = response.json()

print(f"Ваш IP-адрес: {data['ip']}")