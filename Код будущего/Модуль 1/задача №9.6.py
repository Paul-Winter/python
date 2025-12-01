# Задача №9:
# Переставьте в списке минимальное и максимальное числа местами.

number = int(input("Введите количество чисел: "))
my_list = []
for i in range(number):
    my_list.append(int(input("Введите число: ")))
print(my_list)
minimum = min(my_list)
max_index = my_list.index(max(my_list))
print(minimum)
print(max_index)
my_list[my_list.index(min(my_list))] = max(my_list)
my_list[max_index] = minimum
print(my_list)
