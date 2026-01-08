# фильтрация и экспорт
# - найти, сколько уязвимостей у каждого IP
# - вывести топ-3 IP с наибольшим числом уязвимостей
# - сохранить в новый файл уязвимости с уровнем Critical
# - определить, какие уязвимости встречаются чаще всего (по CVE)
import os
import csv

os.chdir("C:\\Users\\Student\\python\\Код будущего\\test")

with open("vulns.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    dict = {}
    for row in reader:
        if row[2] in dict:
            dict[row[2]] = dict[row[2]] + 1
        else:
            dict[row[2]] = 1
items = dict.items()
sorted_items = sorted(items,key=lambda item: item[1], reverse=True)
for k,v in sorted_items:
    print(f"{k} - {v}")
