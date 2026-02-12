import requests

ip = input("Введите IP-адрес (8.8.8.8): ")
url = f"http://ip-api.com/json/{ip}"
response = requests.get(url)
data = response.json()

# if response.status_code == 200:
if data.get("status") == "success":
    print("IP", ip)
    print("Страна", data['country'])
    print("Город:", data['city'])
    print(f"Координаты: {data['lat']}, {data['lon']}")
else:
    print("Ошибка: Не удалось получить данные для этого IP.")
