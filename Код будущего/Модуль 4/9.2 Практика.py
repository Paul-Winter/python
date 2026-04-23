# Создайте скрипт, который анализирует лог-файл авторизации для выявления пользователей, пытавшихся войти в систему, подсчитывает частоту попыток по IP-адресам и пользователям, формирует отчет в формате CSV, визуализирует результаты графиком и создает уведомления при обнаружении пиковых нагрузок.

#### Пояснение к задаче
# 1. Импортируй необходимые модули:
#    - `re` для работы с регулярными выражениями
#    - `Counter` из `collections` для подсчета частоты
#    - `csv` для генерации отчета
#    - `matplotlib.pyplot` для построения графика
#    - `datetime` из `datetime` для работы с временными метками
# 2. Открой файл `'4/4.9/4.auth.log'` в режиме чтения с кодировкой `utf-8` и прочитай все строки.
# 3. Составь регулярные выражения:
#    - Для поиска IP-адреса: `r'(\d+\.\d+\.\d+\.\d+)'`
#    - Для поиска имени пользователя: `r'for (?:invalid user )?(\w+)'` (обрабатывает как обычных пользователей, так и invalid user)
#    - Для поиска временной метки: `r'\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})'`
# 4. Создай объекты:
#    - `ip_counter` — для подсчета попыток по IP
#    - `user_counter` — для подсчета попыток по пользователю
#    - `combined_counter` — для подсчета попыток по паре (IP, пользователь)
#    - `ip_timeline` — словарь для хранения временных меток каждого IP
# 5. С помощью цикла `for` перебери все строки лога.
# 6. Проверь, содержится ли в строке фраза `'Failed password'` или `'Accepted password'` (признаки попытки входа).
# 7. Если условие выполнено:
#    - Найди IP-адрес с помощью `re.search()`. Если IP найден, извлеки его, иначе присвой значение `'Unknown'`.
#    - Найди имя пользователя с помощью `re.search()` с флагом `re.IGNORECASE`. Если пользователь найден, извлеки его, иначе присвой значение `'Unknown'`.
#    - Увеличь счетчики: `ip_counter[ip]`, `user_counter[user]`, `combined_counter[(ip, user)]`.
#    - Извлеки временную метку из строки. Если временная метка найдена и IP не равен `'Unknown'`, преобразуй её в объект `datetime` с помощью `datetime.strptime()` и формата `'%d/%b/%Y:%H:%M:%S'`, затем добавь в список временных меток для соответствующего IP в словаре `ip_timeline`.
# 8. Выведи статистику:
#    - Топ-10 IP-адресов в формате: `f'IP {ip}: попыток {count}'`
#    - Топ-10 пользователей в формате: `f'User {user}: попыток {count}'`
# 9. Построй гистограмму для топ-10 IP-адресов:
#    - По оси X — IP-адреса
#    - По оси Y — количество попыток
#    - Поверни подписи оси X на 45 градусов
#    - Добавь заголовок: `'Топ-10 IP-адресов по количеству попыток доступа'`
#    - Примени `tight_layout()` и отобрази график с помощью `plt.show()`
# 10. Создай систему уведомлений для обнаружения пиковых нагрузок:
#     - Задай порог общего количества попыток для IP: `THRESHOLD = 50`
#     - Открой файл `'alerts.log'` в режиме добавления (`'a'`) с кодировкой `utf-8`
#     - Для каждого IP в `ip_timeline`:
#       - Если количество попыток превышает порог, проверь минутные интервалы
#       - Отсортируй временные метки по возрастанию
#       - Для каждой временной метки подсчитай количество запросов в течение следующих 60 секунд
#       - Если количество запросов в любом минутном интервале превышает 20, запиши уведомление в формате: `f"[ALERT] {datetime.now()} | IP {ip} совершил {count} попыток в минуту | Всего: {len(times)} попыток\n"`
#       - Выведи уведомление в консоль и запиши в файл `alerts.log`
#       - Прерви проверку для этого IP после первого обнаружения пика
# 11. Сформируй отчет в формате CSV:
#     - Открой файл `'report.csv'` в режиме записи с параметрами `newline=''` и `encoding='utf-8'`
#     - Создай объект `writer` с разделителем `'|'`
#     - Запиши заголовок: `['IP', 'User', 'Attempts']`
#     - С помощью `most_common()` перебери пары (IP, пользователь) в порядке убывания количества попыток и запиши каждую строку в CSV-файл


import re
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter

# Чтение лога
with open('4/4.9/4.auth.log', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Регулярные выражения
ip_pattern = r'(\d+\.\d+\.\d+\.\d+)'
user_pattern = r'for (?:invalid user )?(\w+)'
time_pattern = r'\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})'

# Счетчики
ip_counter = Counter()
user_counter = Counter()
combined_counter = Counter()
ip_timeline = {}

# Обработка строк лога
for line in lines:
    if 'Failed password' in line or 'Accepted password' in line:
        # Извлечение IP
        ip_match = re.search(ip_pattern, line)
        ip = ip_match.group(1) if ip_match else 'Unknown'
        
        # Извлечение пользователя
        user_match = re.search(user_pattern, line, re.IGNORECASE)
        user = user_match.group(1) if user_match else 'Unknown'
        
        # Обновление счетчиков
        ip_counter[ip] += 1
        user_counter[user] += 1
        combined_counter[(ip, user)] += 1
        
        # Извлечение времени для динамики
        time_match = re.search(time_pattern, line)
        if time_match and ip != 'Unknown':
            time_str = time_match.group(1)
            log_time = datetime.strptime(time_str, '%d/%b/%Y:%H:%M:%S')
            if ip not in ip_timeline:
                ip_timeline[ip] = []
            ip_timeline[ip].append(log_time)

# Вывод статистики в консоль
print("=== Статистика по IP-адресам ===")
for ip, count in ip_counter.most_common(10):
    print(f'IP {ip}: попыток {count}')

print("\n=== Статистика по пользователям ===")
for user, count in user_counter.most_common(10):
    print(f'User {user}: попыток {count}')

# Визуализация: топ-10 IP
plt.figure(figsize=(12, 6))
top_ips = ip_counter.most_common(10)
ips = [item[0] for item in top_ips]
counts = [item[1] for item in top_ips]
plt.bar(ips, counts, color='skyblue')
plt.xlabel('IP-адреса')
plt.ylabel('Количество попыток')
plt.title('Топ-10 IP-адресов по количеству попыток доступа')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Проверка пиковых нагрузок и уведомления
THRESHOLD = 50
ALERT_MINUTE_THRESHOLD = 20

with open('alerts.log', 'a', encoding='utf-8') as alert_file:
    for ip, times in ip_timeline.items():
        if len(times) > THRESHOLD:
            times.sort()
            for i in range(len(times)):
                count = 1
                for j in range(i + 1, len(times)):
                    if (times[j] - times[i]).total_seconds() < 60:
                        count += 1
                    else:
                        break
                if count > ALERT_MINUTE_THRESHOLD:
                    alert_msg = (f"[ALERT] {datetime.now()} | "
                                f"IP {ip} совершил {count} попыток в минуту | "
                                f"Всего: {len(times)} попыток\n")
                    print(alert_msg.strip())
                    alert_file.write(alert_msg)
                    break

# Сохранение отчета в CSV
with open('report.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(['IP', 'User', 'Attempts'])
    for (ip, user), count in combined_counter.most_common():
        writer.writerow([ip, user, count])

print("\nОтчет сохранен в report.csv")
print("Уведомления записаны в alerts.log")
