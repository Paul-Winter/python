# Напишите программу, которая анализирует главную страницу сайта https://lenta.ru/ и извлекает из него заголовки,
# которые содержат слово "Россия".

#### Пояснения к задаче
# Используйте GET-запрос с помощью библиотеки requests для получения исходного кода страницы https://lenta.ru/.
# Найдите все заголовки h1, h2, h3 и отфильтруйте из них те, в которых встречается слово “Россия”.
# Полученный список выведите на экран.

import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://lenta.ru/"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers, verify=False)
soup = BeautifulSoup(response.text, "lxml")

# Ищем заголовки h1, h2, h3
headers_list = soup.find_all(['h1', 'h2', 'h3'])

word_to_find = "Россия"
count = 0

for header in headers_list:
    text = header.get_text(strip=True)
    if word_to_find.lower() in text.lower():
        count += 1
        print(f"{count}. {text}")

if count == 0:
    print(f"Новостей со словом '{word_to_find}' сейчас нет.")
