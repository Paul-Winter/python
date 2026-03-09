# Напишите программу, которая на сайте Пушкинского музея https://www.pushkinmuseum.ru/ найдет все изображения,
# извлечет URL этих изображений и выведет полученный список  в консоль.

#### Пояснения к задаче
# Для получения кода страницы https://www.pushkinmuseum.ru/ используйте уже хорошо знакомый метод get из модуля requests.
# Изображения определены тегом <img src=...>, где значение src и есть искомый URL.
# Но так как этот же тег может включать ссылки не только непосредственно на изображения, но и на какие-то генерирующие их скрипты,
# обязательно отфильтруйте только те ссылки, которые ведут на файлы с расширениями .jpg, .jpeg, .png

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib3

# Отключаем предупреждения SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.pushkinmuseum.ru/"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    # Делаем запрос (verify=False помогает, если у сайта проблемы с сертификатами)
    response = requests.get(url, headers=headers, verify=False, timeout=10)
    soup = BeautifulSoup(response.content, 'lxml')

    print(f"--- Список изображений с сайта {url} ---")

    # Ищем все теги <img>
    for img in soup.find_all('img'):
        src = img.get('src')

        if src:
            # Проверяем расширения
            if src.lower().endswith(('.jpg', '.jpeg', '.png')):
                # Превращаем относительную ссылку в абсолютную
                full_url = urljoin(url, src)
                print(full_url)

except Exception as e:
    print(f"Произошла ошибка: {e}")
