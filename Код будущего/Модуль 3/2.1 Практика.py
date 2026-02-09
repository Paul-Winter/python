import requests

response = requests.get("https://api.github.com", verify=False)
print(response.status_code)
print(response.text)

#"https://tproger.ru/articles/top-55-cursov-python--onlajn-obuchenie-dlya-razrabotchikov-s-nulya-besplatno-i-platno"
