# найти, сколько строк содержат слово "ERROR"
count = 0
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            count += 1
print(count)
