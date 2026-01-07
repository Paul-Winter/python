# логирование исключений в файл:
# - изменить предыдущую программу так, чтобы в случае ошибки
#   сообщение записывалось в лог-файл

# import datetime
# from datetime import datetime
# datetime.now()

def input_float(type):
    while True:
        try:
            x = float(input("Введите " + type + ": "))
        except ValueError:
            with open("log.txt", "a", encoding="UTF-8") as file:
                file.write("Введено не число\n")
        else:
            break
    return x

a = input_float("делимое")
b = input_float("делитель")

try:
    print(a/b)
except ZeroDivisionError:
    with open("log.txt", "a", encoding="UTF-8") as file:
        file.write("Нельзя делить на ноль\n")