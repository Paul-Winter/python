# Создайте скрипт, который анализирует файл лога авторизации SSH,
# подсчитывает количество неудачных попыток входа по IP-адресам
# и сохраняет результаты в CSV-файл.

#### Пояснение к задаче
# 1. Используйте для анализа модули работы с регулярными выражениями `re`
# и `Counter` из `collections` для подсчета частоты.
# Для работы с CSV-файлами используйте модуль `csv`.
# 2. Лог для анализа находится в файле `'auth.log'`.
# 3. Признаками неудачной авторизации являются сообщения `'Failed password'` или `'Invalid user'`.
# 4. В каждой строке, где содержатся эти слова, найдите IP-адрес.
# Проще всего сделать это с регулярным выражением `r'(\d{1,3}\.){3}\d{1,3}'`.
# 5. После обработки всех строк, откройте на запись файл `ssh_failed_attempts.csv` с параметрами:
#    - `'w'` — режим записи
#    - `newline=''` — для корректной записи строк в CSV
#    - `encoding='utf-8'` — кодировка
# 6. Запишите заголовок CSV-файла с помощью `writer.writerow(['IP address', 'Failed Attempts'])`.
# 7. С помощью метода `most_common()` переберите IP-адреса в порядке убывания количества попыток
# и для каждого IP запишите строку с IP-адресом и количеством попыток.


import re
import csv
from collections import Counter

def analyze_ssh_to_csv(log_filename, output_filename):
    # Объект для подсчета неудачных попыток
    failed_auth = Counter()
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
  
    try:
        # 1. Анализ лога
        with open(log_filename, 'r', encoding='utf-8') as file:
            for line in file:
                if 'Failed password' in line or 'Invalid user' in line:
                    match = re.search(ip_pattern, line)
                    if match:
                        ip = match.group()
                        failed_auth[ip] += 1
      
        # 2. Сохранение результатов в CSV
        with open(output_filename, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Записываем заголовок
            writer.writerow(['IP address', 'Failed Attempts'])
          
            # Записываем данные в порядке убывания
            for ip, count in failed_auth.most_common():
                writer.writerow([ip, count])
              
        print(f"Анализ завершен. Результаты сохранены в {output_filename}")
          
    except FileNotFoundError:
        print(f"Ошибка: Файл {log_filename} не найден")

if __name__ == "__main__":
    analyze_ssh_to_csv('auth.log', 'ssh_failed_attempts.csv')
