# начальный уровень
import csv

with open("data.csv", "r") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        print(dict(row))
