# Чтение текстового файла
# - открыть файл data.txt
# - построчно вывести его содержимое
# - подсчитать общее количество строк в файле
import os
os.chdir("C:\\test")    #???
with open("data.txt", "r") as file:
    i = 0
    for line in file:
        print(line, end="")
        i = i + 1
    print()
    print(i)

    