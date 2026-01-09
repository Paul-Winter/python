# чтение текстового файла:
# - открыть файл data.txt
# - построчно вывести его содержимое
# - подсчитать общее количество строк в файле
with open("data.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())

print(len(lines))
