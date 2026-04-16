# Создайте скрипт, который анализирует файл лога авторизации `auth.log`,
# подсчитывает частоту появления IP-адресов,
# выявляет IP с количеством запросов более 500 и строит график полученных результатов.

#### Пояснение к задаче
# 1. Импортируйте необходимые модули:
#    - `Counter` из `collections` для подсчета частоты
#    - `matplotlib.pyplot` для построения графика
#    - `re` для работы с регулярными выражениями
# 2. Откройте файл `'auth.log'` в режиме чтения с кодировкой `utf-8` и прочитайте все строки.
# 3. Составьте регулярное выражение для поиска IP-адресов: `r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'`.
# 4. Создайте пустой список `ip_addresses`. Для каждой строки лога найдите все IP-адреса с помощью `re.findall()` и добавь их в список.
# 5. Создайте объект `Counter` из списка `ip_addresses` для подсчета частоты встречаемости каждого IP.
# 6. Задайте пороговое значение `500`. Отфильтруйте IP-адреса, оставив только те, у которых количество запросов превышает порог.
# 7. Выведите результаты в формате: `"IP-адреса с более чем {threshold} запросами:"`, затем для каждого IP выведи `"{ip}: {count} запросов"`. Если таких IP нет, выведите сообщение: `"Нет IP с частотой более 500 запросов"`.
# 8. Если есть IP, превышающие порог, отсортируй их по убыванию количества запросов.
# 9. Постройте гистограмму:
#    - По оси X — IP-адреса
#    - По оси Y — количество запросов
#    - Поверни подписи оси X на 45 градусов для удобства чтения
#    - Добавь заголовок: `"IP > {threshold} запросов"`
#    - Примени `tight_layout()` для автоматической настройки отступов
#    - Отобрази график с помощью `plt.show()`

from collections import Counter
import matplotlib.pyplot as plt
import re

# Читаем файл
with open('auth.log', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Ищем IP-адреса
ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
ip_addresses = []

for line in lines:
    ip_addresses.extend(re.findall(ip_pattern, line))

# Считаем частоту
ip_counter = Counter(ip_addresses)

# Фильтруем (>500)
threshold = 500
high_ips = {ip: count for ip, count in ip_counter.items() if count > threshold}

# Выводим результаты
print(f"IP-адреса с более чем {threshold} запросами:")
if high_ips:
    # Сортируем и выводим
    sorted_items = sorted(high_ips.items(), key=lambda x: x[1], reverse=True)
    for ip, count in sorted_items:
        print(f"{ip}: {count} запросов")
    
    # Строим график
    ips = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]
    
    plt.bar(ips, counts)
    plt.xticks(rotation=45)
    plt.title(f'IP > {threshold} запросов')
    plt.tight_layout()
    plt.show()
else:
    print("Нет IP с частотой более 500 запросов")
