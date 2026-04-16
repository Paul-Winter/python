# Создайте скрипт, который анализирует файл лога авторизации `auth.log`, подсчитывает частоту появления IP-адресов, выявляет IP с количеством запросов более 500 и строит график полученных результатов.

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

import re
import matplotlib.pyplot as plt
from collections import Counter

def analyze_auth_logs(filename):
    threshold = 500
    ip_addresses = []
  
    # Регулярное выражение для IPv4
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
  
    try:
        # 2. Чтение файла
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # 4. Поиск IP
                found_ips = re.findall(ip_pattern, line)
                ip_addresses.extend(found_ips)
      
        # 5. Подсчет частоты
        ip_counts = Counter(ip_addresses)
      
        # 6. Фильтрация по порогу
        suspicious_ips = {ip: count for ip, count in ip_counts.items() if count > threshold}
      
        if not suspicious_ips:
            print(f"Нет IP с частотой более {threshold} запросов")
            return

        # 7. Вывод результатов
        print(f"IP-адреса с более чем {threshold} запросами:")
      
        # 8. Сортировка по убыванию
        sorted_ips = sorted(suspicious_ips.items(), key=lambda item: item[1], reverse=True)
      
        ips = []
        counts = []
      
        for ip, count in sorted_ips:
            print(f"{ip}: {count} запросов")
            ips.append(ip)
            counts.append(count)
      
        # 9. Построение гистограммы
        plt.figure(figsize=(10, 6))
        plt.bar(ips, counts, color='crimson')
      
        plt.title(f"IP > {threshold} запросов")
        plt.xlabel("IP-адреса")
        plt.ylabel("Количество запросов")
      
        # Поворот подписей
        plt.xticks(rotation=45)
      
        plt.tight_layout()
        plt.show()
          
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден")

if __name__ == "__main__":
    analyze_auth_logs('auth.log')
