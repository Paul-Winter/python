# простое деление с защитой от нуля:
# - запросить у пользователя два числа и вывести результат деления
# - если происходит деление на ноль - вывести сообщение об ошибке

while True:
    try:
        a = float(input("Введите делимое: "))
    except ValueError:
        print("Введено не число")
    else:
        break
while True:
    try:
        b = float(input("Введите делитель: "))
    except ValueError:
        print("Введено не число")
    else:
        break
try:
    print(a/b)
except ZeroDivisionError:
    print("Нельзя делить на ноль!")