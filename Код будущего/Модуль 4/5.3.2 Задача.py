# Разработайте скрипт, который выводит список всех запущенных процессов, проверяет их на наличие в чёрном списке (например, ncat, reverse_shell, mimikatz и др.) и завершает обнаруженные процессы. Уведомления о завершении выводите в терминал.

#### Пояснение к задаче
# 1. Используйте библиотеку  psutil для получения информации о запущенных процессах 
# 2. Создайте список подозрительных процессов (например, ncat, netcat, nc.exe, reverse_shell, backdoor, mimikatz, wireshark, tcpview, procdump)
# 3. Создайте функцию, которая будет выводить уведомления 
# 4. Переберите все запущенные процессы, используя `psutil.process_iter()` для получения информации о процессах
# 5. Проверьте каждый процесс на подозрительность сверяясь со списком подозрительных процессов. Если процесс подозрительный, выведите об этом уведомление с указанием названия и завершите этот процесс
# 6. Обработайте исключения, игнорируя ошибки, если процесс уже завершен или нет доступа

import psutil
import subprocess

suspicious_processes = [
    'ncat', 'netcat', 'nc.exe', 'reverse_shell', 'backdoor',
    'mimikatz', 'wireshark', 'tcpview', 'procdump'
]

def send_alert(message):
    print(f'Уведомление: {message}')

for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
    try:
        pid = proc.info['pid']
        name=proc.info['name']
        is_warning=False
        for susp in suspicious_processes:
            if susp.lower() in name.lower():
                is_warning=True
                break      
        if is_warning:
            send_alert(f'Обнаружен подозрительный процесс: {name}')
            try:
                proc.terminate()
                proc.wait(timeout=3)
                send_alert(f"Процесс {name} мягко завершен")
            except:
                proc.kill()
                send_alert(f"Процесс {name} принудительно завершен")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
