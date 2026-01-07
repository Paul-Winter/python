# Задача №3:
# Написать функцию, которая принимает три параметра:
#  *name - имя человека
#  *surname - фамилия человека
#  *patronymic - отчество человека
# а затем выводит на печать ФИО человека.
# Примечание:
# Предусмотреть тот факт, что все три буквы в ФИО должны иметь верхний регистр.

def fio_func(name, surname, patronymic):
    print(
        f"{surname[0].capitalize()} {name[0].capitalize()} {patronymic[0].capitalize()}")


name = input("Введите имя: ")
surname = input("Введите фамилию: ")
patronymic = input("Введите отчество: ")
fio_func(name, surname, patronymic)
