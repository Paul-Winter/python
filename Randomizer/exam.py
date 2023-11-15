import random

# принять количество вопросов для перемешивания
finish = int(input("Введите общее количество вопросов: "))
# принять количество вопросов в билете
quests = int(input("Введите количество вопросов в билете: "))
# создать массив для 
for_rand_array = [i for i in range(finish)]
total_array = [[]]
array = []
for i in range(len(for_rand_array) - 1):
    for j in range(quests):
        r = random.randint(0, len(for_rand_array) - 1)
        array.append(for_rand_array[r])
        for_rand_array.pop(for_rand_array[r])
    total_array.append(array)
print(total_array)