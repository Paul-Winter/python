# Задача №7:
# На вход программе подаётся натуральное число n.
# Напишите программу, которая создаёт список состоящий из делителей введённого числа

number = int(input("Введите число: "))
my_list = []
for i in range(1, int(number)+1):
    if (number % i == 0):
        my_list.append(i)
print('Делители числа ' + str(number) + ':')
print(my_list)
