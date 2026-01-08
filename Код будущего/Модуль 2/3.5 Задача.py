# часто повторяющиеся уязвимости
# - найти, сколько уязвимостей у каждого IP
# - вывести топ-3 IP с наибольшим числом уязвимостей
# - сохранить в новый файл уязвимости с уровнем Critical
# - определить, какие уязвимости встречаются чаще всего (по CVE)
# - отсортировать уязвимости по убыванию CVSS
import os
import csv

os.chdir("C:\\Users\\Student\\python\\Код будущего\\test")

with open("vulns.csv", newline='', encoding="utf-8") as file:
    reader = csv.reader(file)
    head = next(reader)
    list = []
    for row in reader:
        list.append(row)

sorted_list = sorted(list,key=lambda item: float(item[3]), reverse=True)
with open('vulns2.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(head)
    writer.writerows(sorted_list)
