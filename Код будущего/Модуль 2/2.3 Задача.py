# простой калькулятор с защитой от сбоев. Реализовать калькулятор, который:
# - выполняет сложение, вычитание, умножение и деление
# - не падает при ошибках (деление на ноль, ввод букв вместо чисел)
# - записывает ошибки в лог

def input_float(type):
    while True:
        try:
            x = float(input())
        except ValueError:
            print("Ошибка:введите числа")
            with open("calculator.log", 'a', encoding="UTF-8") as file:
                file.write("введены некорректные данные\n")
        else:
            break
    return x

# with open("calculator.log", 'w', encoding="UTF-8") as file:
#     file.write("Начало работы программы\n")
# print("Добро пожаловать в калькулятор")

while True:
    first = input_float("1 число")
    second = input_float("2 число")
    operation = str(input("Введите необходимое действие (+,-,*,/): "))
    match operation:
        case "+":
            result = first + second
        case "-":
            result = first - second
        case "*":
            result = first * second
        case "/":
            try:
                result = first / second
            except ZeroDivisionError:
               print("Ошибка:деление на ноль")
               with open("calculator.log", 'a', encoding="UTF-8") as file:
                   file.write("деление на ноль\n")
        case _:
            with open("calculator.log", 'a', encoding="UTF-8") as file:
                file.write("Введён неверный код операции\n")
    print(f"Результат: {result}")
    while True:
        ex = input("Выполнить ещё одно вычисление? (y/n)")
        match ex:
            case "y":
                break
            case "n":
                break
            case _:
                print("Введите 'y' или 'n'")
                with open("calculator.log", 'a', encoding="UTF-8") as file:
                    file.write("Введёно недопустимое действие\n")
    if ex == 'n':
        print("Конец работы программы")
        break
