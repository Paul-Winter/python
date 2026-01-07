import os

#os.rename("test1.txt", "test2.txt")

file = open("test2.txt", "r")
print(file.read())
file.close()

with open("test2.txt") as file:
    print(file.read())

# 1. запросить у пользователя строку
# 2. добавить введённую пользователем строку в файл
# 3. прочитать запись из файла в консоль
# 4. обработать исключительную ситуацию обращения к несуществующему файлу
