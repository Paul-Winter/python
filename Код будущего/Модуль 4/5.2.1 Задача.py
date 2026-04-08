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

def monitor_network():
    standard_ports = [80, 443, 21, 22, 25, 110, 143, 3306, 3389, 53]
  
    try:
        connections = psutil.net_connections(kind='inet')
    except Exception:
        return

    print(f"{'Протокол':<8} | {'Локальный адрес':<20} | {'Удаленный адрес':<20} | {'Статус'}")
    print("-" * 75)

    for conn in connections:
        proto = "TCP" if conn.type == socket.SOCK_STREAM else "UDP"
        l_addr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "0.0.0.0:0"
      
        r_addr = "N/A"
        is_suspicious = False
      
        if conn.raddr:
            r_addr = f"{conn.raddr.ip}:{conn.raddr.port}"
            if conn.raddr.port not in standard_ports and conn.raddr.port > 1024:
                is_suspicious = True

        status = "[!] ПОДОЗРИТЕЛЬНО" if is_suspicious else "Норма"
        print(f"{proto:<8} | {l_addr:<20} | {r_addr:<20} | {status}")

if __name__ == "__main__":
    monitor_network()
