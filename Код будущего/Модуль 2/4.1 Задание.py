# Проанализировать JSON-файла с уязвимостями

# 1. Прочитать JSON-файл vulnreport.json.
# 2. Ожидается, что в файле находится список объектов,
#    и каждый объект содержит поле "ip".
# 3. Собрать все IP-адреса, которые встречаются в данных.
# 4. Исключить повторяющиеся IP-адреса.
# 5. Отсортировать IP-адреса по возрастанию.
# 6. Вывести каждый IP-адрес в отдельной строке.
# 7. Если файл vulnreport.json отсутствует, вывести сообщение:
#    Файл vulnreport.json не найден.

import json

input_file="vulnreport.json"
try:
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Файл {input_file} не найден")
    
ips = set()
# ожидаем структуру: список хостов, каждый с полем "ip"
for host in data:
    ip = host.get("ip")
    if ip:
        ips.add(ip)
for ip in sorted(ips):
    print(ip)
