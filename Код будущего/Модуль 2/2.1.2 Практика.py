# запись в новый файл
# - скопировать содержимое data.txt в copy.txt
# - добавить нумерацию строк при записи
import os
os.chdir("C:\\test")    #???
with open("data.txt", "r") as file:
    i = 1
    with open("copy.txt", "w") as copyFile:
        print()
    for line in file:
        with open("copy.txt", "a+") as copyFile:
            copyFile.write(str(i) + ": " + line)
        i = i + 1
        