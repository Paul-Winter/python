# Разработать программу на Python, которая анализирует отчёт сканера
# уязвимостей (в формате CSV или JSON), находит все критические
# уязвимости и выводит статистику в виде таблицы и графика.

# НАЧАЛЬНЫЙ УРОВЕНЬ
# 1-й вариант
import csv

count = 0
with open("report.csv", encoding="utf-8") as file:
    for line in csv.reader(file):
        if len(line) > 1 and line[1] == "CRITICAL":
            count += 1
print(count)

# НАЧАЛЬНЫЙ УРОВЕНЬ
# 2-й вариант
count = 0
with open("report.csv", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) > 1 and parts[1] == "CRITICAL":
            count += 1
print(count)

# НАЧАЛЬНЫЙ УРОВЕНЬ
# 3-й вариант
with open("report.csv", encoding="utf-8") as file:
    lines = file.readlines()
    critical = [line for line in lines if ",CRITICAL," in line]
print(len(critical))

# БАЗОВЫЙ УРОВЕНЬ
# 1-й вариант
import csv
from collections import Counter

count = Counter()
with open("report.csv", encoding="utf-8") as file:
    for name, level, vuln, desc in csv.reader(file):
        if level == "CRITICAL":
            print(name, desc)
            count[vuln] += 1
for v, c in count.items():
    print(v, c)

# БАЗОВЫЙ УРОВЕНЬ
# 2-й вариант
vulns = {}
with open("report.csv", encoding="utf-8") as file:
    for line in file:
        name, level, vuln, desc = line.strip.split(",")
        if level == "CRITICAL":
            print(name, desc)
            vulns[vuln] = vulns.get(vuln, 0) + 1
for v in vulns:
    print(v, vulns[v])

# БАЗОВЫЙ УРОВЕНЬ
# 3-й вариант
critical = []
vulns = {}
with open("report.csv", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(",")
        if parts[1] == "CRITICAL":
            critical.append(parts)
            vulns[parts[2]] = vulns.get(parts[2], 0) + 1
for c in critical:
    print(c[0], c[3])

for v, n in vulns.items():
    print(v, n)
