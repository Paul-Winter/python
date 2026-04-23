# Создайте скрипт для расследования инцидента информационной безопасности. На сервере под управлением Ubuntu с установленным веб-сервером Apache (открыт порт 80) обнаружена аномальная активность — в логах зафиксированы массовые запросы к файлу `/uploads/shell.php`. Предположительно, злоумышленник использовал уязвимость веб-приложения для загрузки веб-оболочки (web shell), получил удалённый доступ к системе, после чего в логе авторизации `auth.log` появились подозрительные записи.

#### Пояснение к задаче
# 1. Импортируй необходимые модули:
#    - `re` для работы с регулярными выражениями
#    - `Counter` из `collections` для подсчета частоты
#    - `csv` для работы с CSV-файлами
#    - `matplotlib.pyplot` для построения графика
#    - `datetime` из `datetime` для работы с временными метками
#    - `smtplib` и `email.mime.text` для отправки email-уведомлений (опционально)
# 2. Открой файл `'4/4.9/4.auth.log'` в режиме чтения с кодировкой `utf-8` и прочитай все строки.
# 3. Составь регулярные выражения:
#    - Для поиска IP-адреса: `r'(\d+\.\d+\.\d+\.\d+)'`
#    - Для поиска имени пользователя: `r'for (?:invalid user )?(\w+)'`
#    - Для поиска временной метки: `r'(\w+\s+\d+\s+\d+:\d+:\d+)'`
# 4. Создай объекты:
#    - `ip_counter` — для подсчета попыток по IP
#    - `user_counter` — для подсчета попыток по пользователю
#    - `combined_counter` — для подсчета попыток по паре (IP, пользователь)
#    - `time_counter` — для подсчета попыток по часам (агрегированное время)
# 5. С помощью цикла `for` перебери все строки лога.
# 6. Проверь, содержится ли в строке фраза `'Failed password'` или `'Accepted password'` (признаки попытки входа).
# 7. Если условие выполнено:
#    - Найди IP-адрес с помощью `re.search()`. Если IP найден, извлеки его, иначе присвой значение `'Unknown'`.
#    - Найди имя пользователя с помощью `re.search()` с флагом `re.IGNORECASE`. Если пользователь найден, извлеки его, иначе присвой значение `'Unknown'`.
#    - Найди временную метку с помощью `re.search()`. Если временная метка найдена:
#      - Раздели строку на части с помощью `split()`
#      - Сформируй ключ часа в формате: `f'{месяц} {день} {час}:00'` (агрегирование по часам)
#      - Увеличь счетчик `time_counter[hour_key]`
#    - Увеличь счетчики: `ip_counter[ip]`, `user_counter[user]`, `combined_counter[(ip, user)]`
# 8. Построй график временной динамики:
#    - Отсортируй ключи времени в хронологическом порядке
#    - Создай список значений для оси Y
#    - Построй линейный график с маркерами
#    - Добавь заголовок: `'Попытки доступа'`
#    - Подпиши оси: X — `'Время'`, Y — `'Попытки'`
#    - Поверни подписи оси X на 45 градусов
#    - Добавь сетку с прозрачностью 0.3
#    - Отобрази график с помощью `plt.show()`
# 9. Обнаружение аномалий и отправка уведомлений:
#    - Задай пороговое значение `porog = 55` (количество попыток в час)
#    - Создай список `alerts` для хранения предупреждений
#    - Для каждого часа в `time_counter`, если количество попыток превышает порог, добавь запись в формате: `f'{time_hour} | {count} попыток'`
#    - Если есть предупреждения, выведи их в консоль
#    - (Опционально) Отправь email-уведомление администратору:
#      - Создай объект `MIMEText` с текстом предупреждения
#      - Установи тему, отправителя и получателя
#      - Подключись к SMTP-серверу, выполни аутентификацию и отправь сообщение
# 10. **Анализ для определения IP атакующего:**
#     - Выведи топ-10 IP-адресов с наибольшим количеством попыток
#     - Выведи топ-10 пользователей, которые были целью атаки
#     - Определи IP с наибольшим количеством успешных входов (`Accepted password`) — вероятный IP атакующего
#     - Выведи комбинированную статистику по парам (IP, пользователь)


import re
import csv
import smtplib
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter
from email.mime.text import MIMEText

# Чтение лога
with open('4/4.9/4.auth.log', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Регулярные выражения
ip_pattern = r'(\d+\.\d+\.\d+\.\d+)'
user_pattern = r'for (?:invalid user )?(\w+)'
time_pattern = r'(\w+\s+\d+\s+\d+:\d+:\d+)'

# Счетчики
ip_counter = Counter()
user_counter = Counter()
combined_counter = Counter()
time_counter = Counter()
successful_ips = Counter()  # Для отслеживания успешных входов

# Обработка строк лога
for line in lines:
    if 'Failed password' in line or 'Accepted password' in line:
        # Извлечение IP
        ip_match = re.search(ip_pattern, line)
        ip = ip_match.group(1) if ip_match else 'Unknown'
        
        # Извлечение пользователя
        user_match = re.search(user_pattern, line, re.IGNORECASE)
        user = user_match.group(1) if user_match else 'Unknown'
        
        # Отслеживание успешных входов
        if 'Accepted password' in line:
            successful_ips[ip] += 1
        
        # Извлечение времени
        time_match = re.search(time_pattern, line)
        if time_match:
            time_str = time_match.group(1)
            parts = time_str.split()
            hour_key = f'{parts[0]} {parts[1]} {parts[2][:2]}:00'
            time_counter[hour_key] += 1
        
        # Обновление счетчиков
        ip_counter[ip] += 1
        user_counter[user] += 1
        combined_counter[(ip, user)] += 1

# 1. Поиск IP атакующего
print("=== АНАЛИЗ АТАКИ ===\n")

# Топ-10 IP по количеству попыток
print("Топ-10 IP-адресов по количеству попыток:")
for ip, count in ip_counter.most_common(10):
    print(f'  IP {ip}: {count} попыток')

# IP с успешными входами (вероятный атакующий)
print("\nIP-адреса с успешными входами (Accepted password):")
for ip, count in successful_ips.most_common():
    print(f'  IP {ip}: {count} успешных входов')

# Определение подозрительного IP
suspicious_ips = []
for ip, count in successful_ips.items():
    if count > 0 and ip_counter[ip] > 10:
        suspicious_ips.append(ip)
        print(f"\n!!! ПОДОЗРИТЕЛЬНЫЙ IP: {ip} - {count} успешных входов, всего {ip_counter[ip]} попыток")

# 2. Построение timeline событий
if time_counter:
    times = sorted(time_counter.keys())
    counts = [time_counter[t] for t in times]
    
    plt.figure(figsize=(14, 6))
    plt.plot(times, counts, marker='o', linestyle='-', color='red', linewidth=2, markersize=4)
    plt.title('Динамика попыток доступа по часам', fontsize=14)
    plt.xlabel('Время', fontsize=12)
    plt.ylabel('Количество попыток', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# Вывод детального timeline
print("\n=== TIMELINE СОБЫТИЙ ===")
for time_hour, count in sorted(time_counter.items()):
    if count > 20:  # Вывод только значимых часов
        print(f'{time_hour} | {count} попыток')

# 3. Обнаружение аномалий и уведомления
porog = 55
alerts = []

for time_hour, count in time_counter.items():
    if count > porog:
        alerts.append(f'{time_hour} | {count} попыток (превышение порога {porog})')

if alerts:
    print("\n=== ПРЕВЫШЕНИЯ ПОРОГА ===")
    alert_text = ''
    for alert in alerts:
        print(alert)
        alert_text = alert_text + alert + '\n'
    
    # Отправка email-уведомления (раскомментировать для использования)
    # msg = MIMEText(alert_text, 'plain', 'utf-8')
    # msg['Subject'] = 'ALERT: Аномальная активность на сервере'
    # msg['From'] = 'mail@mail.ru'
    # msg['To'] = 'admin@mail.ru'
    # server = smtplib.SMTP('smtp.yandex.ru', 587)
    # server.starttls()
    # server.login('mail@mail.ru', 'secretpass')
    # server.send_message(msg)
    # server.quit()

# Сохранение отчета
with open('attack_report.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(['IP', 'User', 'Attempts'])
    for (ip, user), count in combined_counter.most_common():
        writer.writerow([ip, user, count])

print("\n=== ЗАЩИТНЫЕ МЕРЫ ===")
print("1. Немедленно заблокировать подозрительные IP-адреса:")
for ip in suspicious_ips:
    print(f"   sudo iptables -A INPUT -s {ip} -j DROP")
print("\n2. Удалить веб-оболочку /uploads/shell.php")
print("3. Проверить права доступа к директории uploads")
print("4. Обновить Apache и модули безопасности")
print("5. Настроить WAF (Web Application Firewall)")
print("6. Установить систему обнаружения вторжений (IDS)")
print("7. Изменить все скомпрометированные пароли")
print("8. Настроить мониторинг логов в реальном времени")
print("\nОтчет сохранен в attack_report.csv")
