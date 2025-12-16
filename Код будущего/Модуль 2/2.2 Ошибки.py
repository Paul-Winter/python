def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    # if b != 0:
    #     return a / b
    # else:
    #     print("Попытка деления на ноль! Будьте внимательны!")
    try:
        result = a / b
    except ZeroDivisionError:
        print("Нельзя делить на ноль! Будьте внимательны!")
    else:
        return result

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
operation = input("Введите знак операции: ")

if (operation == "+"):
    print(f"{first} + {second} = {sum(first, second)}")
elif (operation == "-"):
    print(f"{first} - {second} = {sub(first, second)}")
elif (operation == "*"):
    print(f"{first} * {second} = {mul(first, second)}")
elif (operation == "/"):
    print(f"{first} / {second} = {div(first, second)}")
else:
    print("Ошибка ввода! Будьте внимательны!")