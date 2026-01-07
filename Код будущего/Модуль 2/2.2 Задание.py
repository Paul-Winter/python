# логирование исключений в файл:
# - изменить предыдущую программу так, чтобы в случае ошибки сообщение
#   записывалось в лог-файл
try:
    a = float(input())
    b = float(input())

    if b == 0:
        with open("errors.log", "a", encoding="utf-8") as f:
            f.write("Ошибка: деление на ноль\n")
    else:
        print(a / b)
except ValueError:
    with open("errors.log", "a", encoding="utf-8") as f:
        f.write("Ошибка: введите числа\n")
