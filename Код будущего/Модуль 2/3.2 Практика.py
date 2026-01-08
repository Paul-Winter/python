import os
import csv

os.chdir("C:\\Users\\Student\\python\\Код будущего\\Модуль 2")

with open("test2.csv", newline='', encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

data = [
    ['6', 'Владимир','Владимиров','35'],
    ['7', 'Евгений','Евгеньев','40']
]

with open("test2.csv", 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    # writer.writerow(data[0])
    writer.writerows(data[0:])

data2 = [
    {'номер':'8','имя':'Макар','фамилия':'Макаров','возраст':'54'},
    {'номер':'9','имя':'Александр','фамилия':'Александров','возраст':'66'}
]
fieldname = ['номер','имя','фамилия','возраст']
with open("test2.csv", 'a', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldname)
    # writer.writeheader()
    writer.writerows(data2)