# подсчёт статистики
# - найти, сколько уязвимостей у каждого IP
# - вывести топ-3 IP с наибольшим числом уязвимостей
import os
import csv

os.chdir("C:\\Users\\Student\\python\\Код будущего\\test")

with open("vulns.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    dict = {}
    for row in reader:
        if row[0] in dict:
            dict[row[0]] = dict[row[0]] + 1
        else:
            dict[row[0]] = 1
items = dict.items()
sorted_items = sorted(items,key=lambda item: item[1], reverse=True)
print(sorted_items[:3])