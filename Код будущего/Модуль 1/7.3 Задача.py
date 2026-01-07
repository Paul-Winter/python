# Задача №3:
# Есть 3 словаря:
# >>> dict_a = {1:10, 2:20}
# >>> dict_b = {3:30, 4:40}
# >>> dict_c = {5:50, 6:60}
# Напишите программу для слияния нескольких словарей в один.

dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {5: 50, 6: 60}

result = dict_a.copy()
result.update(dict_b)
result.update(dict_c)

# result = {**dict_a, **dict_b, **dict_c}

print(result)
