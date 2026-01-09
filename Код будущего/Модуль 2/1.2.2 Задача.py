# запись в новый файл
# - скопировать содержимое data.txt в copy.txt
# - добавить нумерацию строк при записи
import os
os.chdir("C:\\Users\\Student\\python\\Код будущего\\test")    #???
with open("data.txt", "r") as file:
    i = 1
    with open("copy.txt", "w") as copyFile:
        for line in file:
            copyFile.write(str(i) + ": " + line)
            i = i + 1
