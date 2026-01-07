# запись в новый файл:
# - скопировать содержимое data.txt в copy.txt
# - добавить нумерацию строк при записи
with open("data.txt", "r", encoding="utf-8") as infile:
    with open("copy.txt", "w", encoding="utf-8") as outfile:
        for i, line in enumerate(infile, 1):
            outfile.write(f"{i}: {line}")
