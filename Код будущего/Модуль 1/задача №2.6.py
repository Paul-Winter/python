# Задача №2:
# На вход программе подаётся одно число n.
# Напишите программу, которая выводит список [1,2,3,...,n].

number = int(input("Введите число: "))
my_list = []
for i in range(number):
    my_list.append(i+1)
print(my_list)
