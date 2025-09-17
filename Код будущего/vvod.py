def vvod():
    while True:
        x = input('Введите число: ')
        if x.isdigit():
            break
        else:
            print('Вы ввели не число: ')
    return int(x)