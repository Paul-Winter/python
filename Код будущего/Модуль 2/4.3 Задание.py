# Для каждого порта - напечатать количество уязвимостей

# 1. Прочитать JSON-файл vulnreport.json.
# 2. Ожидается, что в файле находится список объектов, каждый объект представляет
#    хост и может содержать поле "port" и список уязвимостей в поле "vulns"
# 3. Для каждого порта посчитать количество уязвимостей на всех хостах с этим портом.
# 4. Игнорировать объекты без поля "port".
# 5. Вывести на экран количество уязвимостей для каждого порта в формате
#    "порт: количество", по одной строке на порт.
# 6. Порты выводить в порядке возрастания.
# 7. Если файл vulnreport.json отсутствует, вывести сообщение:
#    Файл vulnreport.json не найден.

import json
from collections import Counter

input_file = "vulnreport.json"
try:
    with open(input_file, "r", encoding="utf-8") as f:
        hosts = json.load(f)
except FileNotFoundError:
    print(f"Файл {input_file} не найден")
counts = Counter()
for host in hosts:
    port = host.get("port")
    if port is None:
        continue
    vulns = host.get("vulns", [])
    counts[port] += len(vulns)
for port in sorted(counts.keys()):
    print(f"{port}: {counts[port]}")
