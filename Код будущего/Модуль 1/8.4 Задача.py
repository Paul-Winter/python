# Задача №4:
# Написать функцию, которая принимает одно целое число num
# и выводит на печать сумму его цифр

def sum_nums(number):
    sum = 0
    for i in str(number):
        sum = sum + int(i)
    print(sum)


sum_nums(int(input("Введите число: ")))
