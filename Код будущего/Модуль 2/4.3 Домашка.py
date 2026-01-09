# продвинутый уровень
import csv
import json

try:
    with open("data.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        data = []
        for row in csv_reader:
            row_dict = dict(row)
            print(row_dict)
            data.append(row_dict)
    
    data = [row for row in data if int(row["Age"]) >= 15]
    data.sort(key=lambda x: int(x["Age"]))

    with open("output.txt", "w") as json_file:
        json.dump(data, json_file, indent=4)

except FileNotFoundError:
    print("Ошибка: Файл data.csv не найден")
