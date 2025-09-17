# Задача №2:
# Написать программу, которая принимает от пользователя год и возвращает
# високосный год или нет.
# Високосный год - год, который кратен 4, но не кратен 100 или кратен 400

def is_year_visokos(year):
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    else:
        return False


print(is_year_visokos(int(input("Введите год: "))))
