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


# ssh_failed_attempts.csv
import csv
import re
from collections import Counter

failed_auth = Counter()
with open('auth.log', 'r', encoding='utf-8') as file:
    for line in file:
        if 'Failed password' in line or 'Invalid user' in line:
            ip_match = re.search(r'(\d{1,3}\.){3}\d{1,3}', line)
            if ip_match:
                ip = ip_match.group()
                failed_auth[ip]+=1

with open('ssh_failed_attempts.csv', 'w', newline='', encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerow(['IP address','Failed Attempts'])
    for ip,count in failed_auth.most_common():
        writer.writerow([ip,count])
