# фильтрация и экспорт
# - найти, сколько уязвимостей у каждого IP
# - вывести топ-3 IP с наибольшим числом уязвимостей
# - сохранить в новый файл уязвимости с уровнем Critical
import os
import csv

os.chdir("C:\\Users\\Student\\python\\Код будущего\\test")

with open("vulns.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    with open("logcritical.csv", 'w', newline='', encoding='utf-8') as file2:
        writer = csv.writer(file2)
        writer.writerow(next(reader))

    # dict = {}
    for row in reader:
        if row[4] == 'Critical':
            with open("logcritical.csv", 'a', newline='', encoding='utf-8') as file2:
                writer = csv.writer(file2)
                writer.writerow(row)

with open("logcritical.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
#         if row[0] in dict:
#             dict[row[0]] = dict[row[0]] + 1
#         else:
#             dict[row[0]] = 1
# items = dict.items()
# sorted_items = sorted(items,key=lambda item: item[1], reverse=True)
# print(sorted_items[:3])