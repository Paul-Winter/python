import requests

response = requests.get("https://httpbin.org/html", verify=False)
print(response.text.find('<h1>'))