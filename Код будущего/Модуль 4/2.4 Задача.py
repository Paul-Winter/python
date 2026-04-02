# Shodan – это поисковая система для устройств, подключенных к интернету.
# Специалисты по ИБ используют его для аудита внешнего периметра компании.
# Ваша задача состоит в том, чтобы автоматизировать сбор информации о домене с помощью Shodan API.

# Интегрируя Shodan API для сканирования периметра, напишите скрипт, который:
# - Принимает на вход домен компании.
# - Через Shodan API находит все открытые порты на этом домене.
# - Выводит список и характеристики этих портов
# Получите API-ключ от Shodan заранее (потребуется регистрация)

#### Пояснения к задаче
# Задайте домен компании Ростелеком: rt.com 
# Создайте переменную domain, в которой хранится доменное имя, и переменную для API-ключа Shodan.
# Сформируйте GET-запрос к API Shodan:
# URL: https://api.shodan.io/shodan/host/search 
# Параметры: key (ваш ключ) и query (поисковый запрос вида hostname:google.com).
# Получите ответ в формате JSON. В разделе matches будут все найденные хосты.
# Для каждого найденного хоста извлеките и выведите:
# - IP-адрес
# - Порт
# - Организацию (org)
# - Сервис (product)
# - Баннер (первые 100 символов ответа сервера)

import requests

# 1. Настройки
domain = "rt.ru"
api_key = "API_KEY"  # нужно получить его на shodan.io
url = "https://api.shodan.io/shodan/host/search"

params = {
   "key": api_key,
   "query": f"hostname:{domain}"
}

try:
    response = requests.get(url, params=params)
  
    if response.status_code == 200:
        data = response.json()
        matches = data.get("matches", [])
      
        print(f"Результаты для {domain}:")
        for host in matches:
            # Выводим данные строго по ТЗ
            print(f"IP: {host.get('ip_str')}")
            print(f"Порт: {host.get('port')}")
            print(f"Организация: {host.get('org')}")
            print("-" * 20)
    else:
        print(f"Ошибка API: {response.status_code}")
except Exception as e:
    print(f"Ошибка: {e}")
