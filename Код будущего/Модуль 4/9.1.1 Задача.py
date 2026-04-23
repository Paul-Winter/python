# Создайте скрипт, который извлекает все уникальные IP-адреса из логов веб-сервера (например, access.log) и фильтрует те, которые совершили более 100 запросов за минуту (признак брутфорса).

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
from datetime import datetime

with open('access.log','r',encoding='utf-8') as file:
    lines = file.readlines()
ip_requests = {}
log_pattern = r'(\d+\.\d+\.\d+\.\d+).*\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})'
for line in lines:
    match = re.search(log_pattern,line)
    if match:
        ip = match.group(1)
        time_str = match.group(2)
        log_time = datetime.strptime(time_str, '%d/%b/%Y:%H:%M:%S')
        if ip not in ip_requests:
            ip_requests[ip]=[]
        ip_requests[ip].append(log_time)
ips=[]
for ip, times in ip_requests.items():
    times.sort()
    for i in range(len(times)):
        count = 1
        for j in range(i+1, len(times)):
            if (times[j]-times[i]).total_seconds() < 60:
                count += 1
            else:
                break
        if count > 100:
            ips.append(ip)
            break
for ip in ips:
    print(ip)
