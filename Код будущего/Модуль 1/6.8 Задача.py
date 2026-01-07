# Задача №8:
# На вход программе подаётся натуральное число n, а затем n целых чисел.
# Напишите программу, которая создаёт из указанных чисел список,
# затем удаляет все элементы стоящие по нечётным индексам, а затем выводит полученный список.

number = int(input("Введите количество чисел: "))
my_list = []
for i in range(number):
    my_list.append(int(input("Введите число: ")))
print(my_list)
last_index = number - 1
if (last_index % 2 == 0):
    j = last_index - 1
else:
    j = last_index
for i in range(j, 0, -2):
    my_list.pop(i)
print(my_list)
