import os
import json

os.chdir("C:\\Users\\Student\\python\\Код будущего\\test")
with open("test.json", encoding="utf-8") as file:
    data = json.load(file)
print(data)
print(len(data))
print(data[0]["age"])
for element in data:
    print(f"{element["name"]} {element["age"]}")

with open("out.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)