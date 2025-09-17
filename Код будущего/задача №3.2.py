# Задача №3:
# Написать программу проверки: является ли год високосным

year = int(input("Введите год: "))
bool1 = year % 4 == 0
bool2 = year % 100 == 0
bool3 = year % 400 == 0
print(bool3 or (bool1 and not (bool2)))
