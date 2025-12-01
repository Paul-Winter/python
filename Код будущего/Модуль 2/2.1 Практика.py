import os

#os.rename("test1.txt", "test2.txt")

# file = open("test2.txt")
# print(file.read())
# file.close()

# 1. запросить у пользователя строку
# 2. добавить введённую пользователем строку
#    в файл

with open("test2.txt") as file:
    print(file.read())