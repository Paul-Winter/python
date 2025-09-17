# Задача №1:
# Написать программу, проверяющую является ли строка палиндромом.
# Палиндром - строка, которая читается одинаково, как слева направо,
# так и наоборот. Например, слово шалаш

str = input("Введите строку для проверки: ")
str_reverse = ''
for i in range(-1, -len(str)-1, -1):
    str_reverse = str_reverse + str[i]
print(str_reverse)
if str.lower() == str_reverse.lower():
    print("Палиндром!")
