import csv

with open("C:\\Users\\Student\\python\\Код будущего\\Модуль 2\\test.csv", newline='', encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("C:\\Users\\Student\\python\\Код будущего\\Модуль 2\\log.csv", newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['level']}\t{row['code']}\t{row["datetime"]}\t{row["message"]}")