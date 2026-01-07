# Задача №2.
# Написать игру "угадай число" (с random)

import random
import vvod

print('Введите первое число из диапазона поиска')
min = vvod.vvod()
print('Введите второе число из диапазона поиска')
max = vvod.vvod()
x = random.randint(min, max)
while True:
    print('Угадайте число из диапазона от ' +
          str(min) + ' до ' + str(max) + ': ')
    user_choice = vvod.vvod()
    if x == user_choice:
        print("Поздравляем! Вы угадали!")
        break
    elif x < user_choice:
        print("Загаданное число меньше!")
        max = user_choice
    elif x > user_choice:
        print("Загаданное число больше!")
        min = user_choice
