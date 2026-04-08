# Напишите скрипт, который выводит список всех активных сетевых соединений (TCP/UDP) и выделяет подозрительные — те, которые используют нестандартные порты (не из списка часто используемых).

#### Пояснение к задаче
# 1. Используйте psutil для получения соединений и socket для определения протокола.
# 2. Получите список активных сетевых соединений
# 3. Создайте список распространенных портов (например, 80, 443, 21, 22, 25, 110, 143, 3306, 3389, 53)
# 4. Для каждого соединения:
# Определите протокол TCP или UDP.
# Получите локальный адрес и порт (если есть) 
# Получите удалённый адрес и порт (если есть)
# 5. Выявите подозрительные соединения – те, которые не входят в список стандартных портов и больше 1024
# 6. Выведите информацию о каждом соединении (как подозрительном, так и нет). Подозрительные соединения пометьте словом "подозрительно"

import psutil
import socket

connects=psutil.net_connections()
common_ports=[80,443,21,22,25,110,143,3306,3389,53]
for conn in connects:
    if conn.type == socket.SOCK_STREAM:
        protocol='TCP'
    else:
        protocol='UDP'
  
    local_addr=f'{conn.laddr.ip}:{conn.laddr.port}' if conn.laddr else 'N/A'
    if conn.raddr:
        remote_addr=f'{conn.raddr.ip}:{conn.raddr.port}'
        remote_port=conn.raddr.port
        if remote_port not in common_ports and remote_port>1024:
            print(f'Подозрительное соединение: {protocol:<6} {local_addr:<30} {remote_addr:<30} {conn.status:<12}')
    else:
        remote_addr='N/A'
        remote_port=None
  
    print(f'Cоединение: {protocol:<6} {local_addr:<30} {remote_addr:<30} {conn.status:<12}')
