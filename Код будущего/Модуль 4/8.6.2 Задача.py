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

def block_malicious_ips(filename):
   threshold = 10
  
   try:
       # 2. Открытие файла
       with open(filename, 'r', encoding='utf-8') as file:
           # 3. Чтение через DictReader
           reader = csv.DictReader(file)
          
           # 4. Перебор строк
           for row in reader:
               # 5. Извлечение данных (используем ключи точно по ТЗ)
               # Если в CSV заголовок 'IP Address', замените 'IP address' ниже
               ip = row['IP address']
               attempts = int(row['Failed Attempts'])
              
               # 6. Проверка порога
               if attempts > threshold:
                   # 7. Формирование команды iptables
                   command = ['iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP']
                  
                   try:
                       # 8. Выполнение команды
                       subprocess.run(command, check=True, capture_output=True)
                      
                       # 9. Сообщение о блокировке
                       print(f"IP {ip} заблокирован")
                      
                   except subprocess.CalledProcessError as e:
                       print(f"Ошибка при блокировке IP {ip}: {e}")
                   except FileNotFoundError:
                       # Если iptables не установлен (например, на Windows)
                       print(f"Команда iptables не найдена. Эмуляция: IP {ip} был бы заблокирован.")
                      
   except FileNotFoundError:
       print(f"Ошибка: Файл {filename} не найден")
   except KeyError as e:
       print(f"Ошибка: В CSV отсутствует столбец {e}")

if __name__ == "__main__":
   block_malicious_ips('ssh_failed_attempts.csv')
