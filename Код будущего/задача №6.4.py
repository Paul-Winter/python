# Задача №6:
# Может ли цикл while работать как for?

count = 0
finish = int(input("Введите количество операций: "))
while count < finish:
    print(str(count + 1) + " операция")
    count += 1