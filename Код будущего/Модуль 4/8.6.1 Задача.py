# Создайте скрипт, который анализирует CSV-файл с результатами проверки неудачных попыток SSH
# и добавляет IP-адреса с подозрительной активностью (более 10 попыток) в черный список через iptables.

#### Пояснение к задаче
# 1. Импортируйте необходимые модули:
#    - `csv` для работы с CSV-файлами
#    - `subprocess` для выполнения системных команд
# 2. Прочитайте из файла `'ssh_failed_attempts.csv'` все строки в виде словарей,
# где ключи — это заголовки столбцов: `'IP address'` для столбца с IP-адресами
# и `'Failed Attempts'` для количество попыток. 
# 3. Для каждого IP-адреса проверьте, превышает ли количество попыток пороговое значение `10`.
# 4. Если превышает, сформируйте команду `iptables` для блокировки IP:
#    - `['iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP']`
#    - `-A INPUT` — добавить правило в цепочку INPUT
#    - `-s ip` — указать исходный IP-адрес
#    - `-j DROP` — действие: отклонить пакеты
# 5. Выполните команду с помощью `subprocess.run()` с параметрами:
#    - `check=True` — вызвать исключение при ошибке
#    - `capture_output=True` — захватить вывод команды
# 6. Выведите сообщение о блокировке в формате: `f'IP {ip} заблокирован'`


import csv
import subprocess

with open('4/4.8/ssh_failed_attempts.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        ip = row['IP address']
        attempts = int(row['Failed Attempts'])
        if attempts > 10:
            cmd = ['iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP']
            subprocess.run(cmd, check=True, capture_output=True)
            print(f'IP {ip} заблокирован')
