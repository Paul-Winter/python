# Напишите программу, которая из веб-страницы:
# https://tproger.ru/articles/top-55-kursov-python--onlajn-obuchenie-dlya-razrabotchikov-s-nulya-besplatno-i-platno
# извлекает все заголовки, а также собирает email-адреса и внешние ссылки.

#### Пояснения к задаче
# Используйте get-запрос для получения кода страницы:
# https://tproger.ru/articles/top-55-kursov-python--onlajn-obuchenie-dlya-razrabotchikov-s-nulya-besplatno-i-platno
# в котором найдите теги заголовков h1 и h2, а также,
# используя полученные на прошлых занятиях навыки использования регулярных выражений,
# все внешние ссылки и email-адреса.

import requests
from bs4 import BeautifulSoup
import re

# Ссылка на статью Tproger
url = "https://tproger.ru/articles/top-55-kursov-python--onlajn-obuchenie-dlya-razrabotchikov-s-nulya-besplatno-i-platno"


response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'lxml')

# 1. Извлекаем заголовки h1 и h2
print("=== ЗАГОЛОВКИ H1 И H2 ===")
for tag in soup.find_all(['h1', 'h2']):
    print(f"{tag.name.upper()}: {tag.get_text(strip=True)}")

# 2. Поиск Email
# Самая простая регулярка для поиска почты
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)
print("\n=== EMAIL-АДРЕСА ===")
for email in set(emails):
    print(email)

# 3. Поиск внешних ссылок
# Ищем все, что начинается на http, но не ведет на сам tproger.ru
links = re.findall(r'https?://[^\s<>"]+', html)
print("\n=== ВНЕШНИЕ ССЫЛКИ ===")
for link in set(links):
    if "tproger.ru" not in link:
        print(link)
