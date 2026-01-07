# чтение файла с защитой от ошибок:
# - написать программу, которая запрашивает у пользователя имя файла и
#   выводит его содержимое построчно
# - если файл не найден - вывести сообщение об ошибке и записать это
#   событие в лог-файл
name = input("Введите имя файла: ")
try:
    with open(name, 'r', encoding="utf-8") as file:
        for line in file:
            print(line)
except FileNotFoundError:
    with open("log2.4.txt", 'w', encoding="UTF-8") as file:
        file.write("Такого файла нет\n")