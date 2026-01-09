# базовый уровень
import csv
import json

with open("data.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    data = []
    for row in csv_reader:
        row_dict = dict(row)
        print(row_dict)
        data.append(row_dict)

with open("output.txt", "w") as json_file:
    json.dump(data, json_file, indent=4)
