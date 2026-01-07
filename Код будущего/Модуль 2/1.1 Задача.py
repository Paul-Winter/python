# Чтение текстового файла
# - открыть файл data.txt
# - построчно вывести его содержимое
# - подсчитать общее количество строк в файле
import os
os.chdir("C:\\test")    #???
with open("data.txt", "r") as file:
    myList = file.readlines()
    file.seek(0,0)
    for i in range(len(myList)):
        print(file.readline(), end="")
    print()
    print(len(myList))
    