# Напишите скрипт на Python, который работает с VirusTotal API:
# - Принимает на вход хеш (MD5/SHA-1/SHA-256) из файла 4.2.1.txt. 
# - Отправляет запрос к VirusTotal API для получения отчета о файле.
# - Выводит количество антивирусных движков, которые считают файл вредоносным
# Для решения задачи получите API-ключ на VirusTotal заранее.
# Помните: у бесплатных ключей есть лимит запросов, поэтому используйте свой собственный ключ.
# #### Примечания к задаче
# - Не забудьте импортировать библиотеки requests и json
# - Ваш API-ключ должен быть занесен в переменную
# - Считайте хэш из файла,  обязательно удалите лишние пробелы и пустые строки
# - Сформируйте запрос к API и проанализируйте ответ. Всю необходимую структуру JSON-ответа можно посмотреть в документации VirusTotal в разделе API response.
# - Посчитайте, сколько антивирусов  посчитали файл вредоносным и выведите ответ на экран
# - Дополнительно посчитайте, сколько всего антивирусов анализировало файл

import requests

# 1. Читаем хеш из файла
with open("4.2.1.txt", "r", encoding="utf-8") as file:
   file_hash = file.read().strip()

# 2. Настройки API
# ВАЖНО: Ученик должен вставить свой ключ
api_key = "9b74c09a7f09cb0664da47812dcfcb808085a82c1e466f2b26bec095f84ccc97"
url = f"https://www.virustotal.com/api/v3/files/{file_hash}"

headers = {
   "accept": "application/json",
   "x-apikey": api_key
}

try:
   # 3. Отправка запроса
   response = requests.get(url, headers=headers)
  
   if response.status_code == 200:
       data = response.json()
      
       # 4. Извлекаем количество движков, пометивших файл как вредоносный
       stats = data['data']['attributes']['last_analysis_stats']
       malicious_count = stats['malicious']
      
       print(f"Файл проверен. Количество угроз: {malicious_count}")
   elif response.status_code == 401:
       print("Ошибка: Неверный API ключ.")
   elif response.status_code == 404:
       print("Ошибка: Хеш не найден в базе VirusTotal.")
   else:
       print(f"Произошла ошибка при запросе: {response.status_code}")

except Exception as e:
   print(f"Ошибка соединения: {e}")
