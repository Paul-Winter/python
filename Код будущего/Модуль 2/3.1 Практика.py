import os
import csv

os.chdir("C:\\Users\\Student\\python\\Код будущего\\Модуль 2")

with open("test.csv", newline='', encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print()

with open("log.csv", newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        print(f"{row['level']}\t{row['code']}\t{row["datetime"]}\t{row["message"]}")

print()

for i in range(256):
    print(f"{bin(i)} - {chr(i)}")