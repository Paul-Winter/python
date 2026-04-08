# Создайте скрипт, который записывает результаты аудита (например, попытки входа, запуск процессов) в файл CSV для дальнейшего анализа.

#### Пояснение к задаче
# 1. Импортируйте необходимые модули
# 2. Создайте имя CSV-файла с временной меткой, используя текущую дату и время в формате `ГГГГММДД_ЧЧММСС`
# 3. Определите заголовки CSV-файла
# 4. Откройте CSV-файл для записи
# 5. Переберите все запущенные процессы
# 6. Запишите информацию о процессе
# 7. Запишите информацию о сетевых соединениях процесса
# 8. Обработайте исключения
# 9. Выведите сообщение о завершении, сообщи пользователю имя созданного CSV-файла

import csv
import psutil
from datetime import datetime
import socket

csv_filename = f'audit_results_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'

csv_headers = ['timestamp', 'event_type', 'username', 'ip_address', 'process_name', 'pid', 'details']

with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
  
    writer.writerow(csv_headers)
  
    for proc in psutil.process_iter(['pid', 'name', 'username', 'connections']):
        try:
            timestamp = datetime.now().isoformat()
            pid = proc.info['pid']
            name = proc.info['name']
            username = proc.info['username']
          
            writer.writerow([timestamp, 'process', username, 'N/A', name, pid, 'Process running'])
          
            try:
                connections = proc.connections()
                for conn in connections:
                    if conn.raddr:
                        details = f'Connection to {conn.raddr.ip}:{conn.raddr.port}'
                        writer.writerow([timestamp, 'network', username, conn.raddr.ip, name, pid, details])
            except:
                pass
              
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

print(f'Данные сохранены в CSV файл: {csv_filename}')
