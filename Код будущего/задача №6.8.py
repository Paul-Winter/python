# Задача №6:
# Написать функцию, которая принимает в качестве аргумента номер месяца
# и возвращает количество дней в данном месяце.

def days_from_month(month):
    if month < 1 or month > 12:
        print("Введите корректный номер месяца!")
        return
    if month == 2:
        return 28
    if month % 2 == 0:
        if month > 7:
            return 31
        else:
            return 30
    else:
        if month > 7:
            return 30
        else:
            return 31


print(days_from_month(int(input("Введите номер месяца: "))))


def from_month_days(month):
    year = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30,
            '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    return year.get(month, "Нет такого месяца!")


print(from_month_days(input("Введите номер месяца: ")))
