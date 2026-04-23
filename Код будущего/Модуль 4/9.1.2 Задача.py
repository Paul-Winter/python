# Создайте скрипт, который извлекает все уникальные IP-адреса из логов веб-сервера (например, access.log)
# и фильтрует те, которые совершили более 100 запросов за минуту (признак брутфорса).

#### Пояснение к задаче
# 1. Используйте модули:
#    - `re` для работы с регулярными выражениями
#    - `datetime` из `datetime` для работы с временными метками
# 2. Логи для анализа находятся в файле `'access.log'`.
# 3. Хранить прочитанные хранения IP-адресов и списки временных меток их запросов для анализа лучше всего при помощи словарей.
# 4. Регулярное выражение для поиска нужный строк лога: `r'(\d+\.\d+\.\d+\.\d+).*\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})'`
#    - Первая группа — IP-адрес
#    - Вторая группа — временная метка в формате `dd/Mon/YYYY:HH:MM:SS`
# 5. Для извлечения данных удобно использовать метод match.group:
#    - IP-адрес с помощью `group(1)`
#    - строку времени с помощью `group(2)`
# 6. Для обработки времени преобразуйте строку времени в объект `datetime` с помощью `datetime.strptime()` и формата `'%d/%b/%Y:%H:%M:%S'`
# 7. Для каждого IP проверьте число запрос с нему за 60 секунд, если оно превышает 100, то добавьте его в список подозрительных.
# 8. Выведите список подозрительных IP-адресов (по одному на строку).


import re
from datetime import datetime, timedelta

def analyze_bruteforce(filename):
    # 3. Словарь для хранения {IP: [timestamps]}
    ip_requests = {}
  
    # 4. Регулярное выражение (IP и метка времени)
    log_pattern = r'(\d+\.\d+\.\d+\.\d+).*\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
  
    try:
        # 2. Чтение файла
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
          
        # 5-7. Парсинг лога
        for line in lines:
            match = re.search(log_pattern, line)
            if match:
                ip = match.group(1)
                time_str = match.group(2)
              
                # Преобразование строки в объект datetime
                # %b — сокращенное название месяца (Jan, Feb...)
                timestamp = datetime.strptime(time_str, '%d/%b/%Y:%H:%M:%S')
              
                if ip not in ip_requests:
                    ip_requests[ip] = []
                ip_requests[ip].append(timestamp)
      
        # 8. Список подозрительных IP
        suspicious_ips = []
      
        # 9. Анализ временных интервалов
        for ip, timestamps in ip_requests.items():
            # Сортируем для корректного замера интервалов
            timestamps.sort()
          
            for i in range(len(timestamps)):
                start_time = timestamps[i]
                end_window = start_time + timedelta(seconds=60)
              
                # Считаем количество запросов в окне 60 секунд
                count = 0
                for t in timestamps[i:]:
                    if t <= end_window:
                        count += 1
                    else:
                        break # Дальше смотреть нет смысла, так как список отсортирован
              
                # Проверка порога в 100 запросов
                if count > 100:
                    suspicious_ips.append(ip)
                    break # IP найден, переходим к следующему
      
        # 10. Вывод результата
        for ip in suspicious_ips:
            print(ip)
          
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден")

if __name__ == "__main__":
    analyze_bruteforce('access.log')
