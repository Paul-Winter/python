# разбор строк лога и группировка по дате
# - извлечь дату из каждой строки
# - подсчитать, сколько событий произошло в каждой дате
import os
os.chdir("C:\\test")    #???
logsinfo = {}
with open("log.txt", "r") as file:
    for line in file:
        date = line[:10]
        if date in logsinfo:
            logsinfo[date] = logsinfo[date] + 1
        else:
            logsinfo[date] = 1
    for key, value in logsinfo.items():
        print(f"В {key} произошло {value} событий")
