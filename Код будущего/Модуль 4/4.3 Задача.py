# Автоматизируйте проверку подозрительного файла 3trojan.exe через публичное API VirusTotal.
# Для этого сначала вычислите хеш файла, затем отправьте запрос к API и проанализируйте ответ.
# Учтите, что если файл ранее не загружался в VirusTotal, вы получите ошибку 404.
# Чтобы проверить известный вредоносный файл, его можно сначала загрузить на сайт VirusTotal вручную, а через 15–30 минут повторить запрос.

#### Пояснения к задаче:
# Импортируйте модули requests (для HTTP-запросов) и hashlib (для хеширования).
# Задайте в переменной key API-ключ VirusTotal c5e21430-3378-4f8e-b9ff-25aa00b877b0
# Откройте в бинарном режиме файл 3trojan.exe, прочитайте содержимое и вычислите SHA-256 хеш.
# Отправьте GET-запрос по адресу https://www.virustotal.com/api/v3/files/{filehash}
# подставив вычисленный хеш и передав в заголовке ключ.
# Проверьте статус ответа:
# Если status_code == 404, выведите сообщение: «Файл в базе VirusTotal не обнаружен».
# Если status_code == 200, извлеките из JSON-ответа статистику last_analysis_stats и выведите количество вредоносных определений (malicious).
# В остальных случаях выведите сообщение об ошибке.

import hashlib
import requests

def check_file_virustotal(filename, api_key):
    # 1. Вычисление SHA-256 хеша файла
    sha256_hash = hashlib.sha256()
    try:
        with open(filename, "rb") as f:
            # Читаем файл порциями, чтобы не забить память
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        file_hash = sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return

    # 2. Подготовка запроса к API v3
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {
        "accept": "application/json",
        "x-apikey": api_key
   }

    # 3. Отправка запроса
    try:
        response = requests.get(url, headers=headers)
      
        if response.status_code == 404:
            print("Файл в базе VirusTotal не обнаружен")
        elif response.status_code == 200:
            data = response.json()
            # Извлекаем статистику последнего анализа
            stats = data['data']['attributes']['last_analysis_stats']
            malicious_count = stats.get('malicious', 0)
            print(f"Результат анализа: обнаружено {malicious_count} вредоносных определений")
        else:
            print(f"Ошибка при запросе к API. Статус-код: {response.status_code}")
          
    except Exception as e:
        print(f"Произошла ошибка при подключении: {e}")

if __name__ == "__main__":
    # Ученик подставляет свой ключ и имя файла
    key = "c5e21430-3378-4f8e-b9ff-25aa00b877b0"
    check_file_virustotal("3trojan.exe", key)
