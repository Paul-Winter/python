# Вам дан CSV-файл 4.2.2.csv с логами веб-сервера.
# В нем три столбца: ip (адрес, с которого пришел запрос), timestamp (время) и request (тип запроса).
# В файле могут встречаться дубликаты.

# С помощью Pandas обработайте этот файл:
# - Удалите дубликаты запросов.
# - Найдите топ-5 IP-адресов с наибольшим количеством запросов.
# - Проверьте эти IP через AbuseIPDB API (или другой сервис) на репутацию. Для этого зарегистрируйтесь на AbuseIPDB, найдите раздел с API-ключами и создайте новый ключ.

#### Пояснения к задаче:
# Считайте файл и с помощью Pandas превратите его в удобную таблицу (DataFrame)
# Уберите дубликаты запросов, используя метод drop_duplicates
# Найдите топ-5 IP-адресов, которые сделали наибольшее количество запросов.
# Для каждого IP из топ-5 отправьте GET-запрос к API. Базовый URL: https://api.abuseipdb.com/api/v2/check.
# В запросе передайте:
# Заголовки: Accept: application/json и ваш key.
# Параметры: ipAddress (проверяемый IP), maxAgeInDays: 90 (проверяем жалобы за 90 дней), verbose (подробный вывод).
# Учтите, что заголовки запроса (headers) можно не создавать заново для каждого IP, а вынести выше, до цикла.
# Получив JSON-ответ, извлеките код страны и общее количество жалоб 
# Выведите на экран для каждого IP: сколько запросов он сделал, его страну и количество жалоб на него.

import pandas as pd
import requests
# 1. Загрузка данных и очистка
df = pd.read_csv('4-2-2.csv')
# Удаляем полные дубликаты строк
df = df.drop_duplicates()

# 2. Поиск топ-5 IP-адресов
# Метод value_counts() возвращает количество вхождений для каждого IP
top_ips = df['ip'].value_counts().head(5)

# 3. Настройка API AbuseIPDB
api_key = 'a2d3baddd345172aba0f2ea1ec559f85c047dd3be9578e49e8ec66eeeb6d4be1ed8a0d4d85bf2bc8'
url = 'https://api.abuseipdb.com/api/v2/check'

headers = {
   'Accept': 'application/json',
   'Key': api_key
}

print("Результаты анализа топ-5 активных IP:")
print("-" * 50)

# 4. Проверка каждого IP через API
for ip, count in top_ips.items():
    params = {
        'ipAddress': ip,
        'maxAgeInDays': '90',
        'verbose': True
    }
  
    try:
        response = requests.get(url, headers=headers, params=params)
      
        if response.status_code == 200:
            data = response.json()['data']
            country = data['countryCode']
            reports = data['totalReports']
          
            print(f"IP: {ip}")
            print(f"  Запросов в логе: {count}")
            print(f"  Страна: {country}")
            print(f"  Жалоб в базе AbuseIPDB: {reports}")
            print("-" * 30)
        else:
            print(f"Ошибка при проверке IP {ip}: статус {response.status_code}")
          
    except Exception as e:
        print(f"Ошибка соединения для IP {ip}: {e}")
