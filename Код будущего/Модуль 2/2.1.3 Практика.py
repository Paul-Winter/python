# найти, сколько строк содержат слово "ERROR"
import os
os.chdir("C:\\test")    #???
with open("data.txt", "r") as file:
    i = 0
    for line in file:
        if "ERROR" in line:
            i = i + 1
    print(i)
    