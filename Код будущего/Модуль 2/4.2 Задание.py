# - найти все уязвимости с CVSS > 8
# - вывести ID и описание

# 1. Прочитать JSON-файл vulnreport.json.
# 2. Ожидается, что в файле находится список объектов, каждый объект
#    представляет хост и можете содержать список уязвимостей в поле "vulns".
# 3. В каждой уязвимости проверить значение поля "cvss".
# 4. Отобрать только те уязвимости, у которых CVSS больше 8.
# 5. Для каждой такой уязвимости получить её "id" и "description".
# 6. Вывести на экран строки в формате "ID: описание",
#    по одной уязвимости на строку.
# 7. Если файл vulnreport.json отсутствует, вывести сообщение:
#    Файл vulnreport.json не найден.

import json

input_file = "vulnreport.json"
try:
    with open(input_file, "r", encoding="utf-8") as f:
        hosts = json.load(f)
except FileNotFoundError:
    print(f"Файл {input_file} не найден")

results = []
for host in hosts:
    for v in host.get("vulns", []):
        try:
            cvss = float(v.get("cvss", 0))
        except (TypeError, ValueError):
            continue
        if cvss > 8:
            vid = v.get("id", "")
            desc = v.get("description", "")
            results.append(f"{vid}: {desc}")
            
for line in results:
    print(line)
