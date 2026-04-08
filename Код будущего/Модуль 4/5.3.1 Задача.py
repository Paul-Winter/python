# Разработайте скрипт, который выводит список всех запущенных процессов, проверяет их на наличие в чёрном списке (например, ncat, reverse_shell, mimikatz и др.) и завершает обнаруженные процессы. Уведомления о завершении выводите в терминал.

#### Пояснение к задаче
# 1. Используйте библиотеку  psutil для получения информации о запущенных процессах 
# 2. Создайте список подозрительных процессов (например, ncat, netcat, nc.exe, reverse_shell, backdoor, mimikatz, wireshark, tcpview, procdump)
# 3. Создайте функцию, которая будет выводить уведомления 
# 4. Переберите все запущенные процессы, используя `psutil.process_iter()` для получения информации о процессах
# 5. Проверьте каждый процесс на подозрительность сверяясь со списком подозрительных процессов. Если процесс подозрительный, выведите об этом уведомление с указанием названия и завершите этот процесс
# 6. Обработайте исключения, игнорируя ошибки, если процесс уже завершен или нет доступа

import psutil

def notify_threat(proc_name, pid):
    """Функция для вывода уведомлений об угрозах"""
    print(f"[!] ОБНАРУЖЕНА УГРОЗА: {proc_name} (PID: {pid})")
    print(f"    Действие: Завершение процесса...")

def monitor_processes():
    # 1. Список подозрительных имен процессов
    blacklist = [
        'ncat', 'netcat', 'nc.exe', 'reverse_shell',
        'backdoor', 'mimikatz', 'wireshark',
        'tcpview', 'procdump'
    ]
  
    print("Запуск сканера активных процессов...")
    print("-" * 40)

    # 2. Перебор всех запущенных процессов
    # Используем attrs=['pid', 'name'], чтобы получить данные за один вызов
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            p_info = proc.info
            p_name = p_info['name'].lower()
            p_pid = p_info['pid']

            # 3. Проверка на вхождение в черный список
            # Проверяем, содержит ли имя процесса любое слово из blacklist
            if any(bad_word in p_name for bad_word in blacklist):
                notify_threat(p_name, p_pid)
              
                # 4. Завершение процесса
                proc.terminate()
                print(f"✅ Процесс {p_pid} успешно остановлен.")
                print("-" * 20)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # 5. Игнорируем ошибки доступа или если процесс уже закрылся
            continue

if __name__ == "__main__":
    monitor_processes()