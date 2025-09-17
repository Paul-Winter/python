# Задача №2:
# Есть список слов, необходимо составить из него строку
#  - через цикл
#  - с помощью метода join

str_list = ['Hello', ',', ' ', 'World', '!']
print(str_list)

result1 = ""
for i in range(len(str_list)):
    result1 += str_list[i]
print(result1)

result2 = "".join(str_list)
print(result2)