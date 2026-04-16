# Создайте скрипт, который обнаруживает аномалии командах bash и находит команды,
# выполняемые чаще среднего значения.

#### Пояснение к задаче
# 1. Для подсчета используйте уже знакомый класс `Counter` из модуля `collections`
# 2. Историю команд прочитайте из файла bash_history.txt в список `command`,
#    выполняя следующие действия:
#    - В каждой прочитанной строке удалите пробелы
#    - Если строка останется не пустой, то добавьте её в список команд 
# 3. Создайте объект `Counter` из списка команд для подсчета частоты встречаемости каждой команды.
# 4. Вычислите общее количество команд (`len(command)`).
# 5. Вычислите количество уникальных команд (`len(cmd_counter)`).
# 6. Рассчитайте среднее значение встречаемости команд:
#    `общее количество / количество уникальных команд`.
# 7. Выведите среднее значение в формате: `"Среднее {average}"`.
# 8. Переберите элементы счетчика. Если количество вхождений команды превышает среднее значение,
#    выведите сообщение в формате: `"Комманда {cmd} встречается чаще среднего, а именно {count} раз"`.

from collections import Counter

with open ('bash_history.txt') as file:
    lines = file.readlines()
command = []
for line in lines:
    clean_line = line.strip()
    if clean_line:
        command.append(clean_line)
cmd_counter = Counter(command)
total_command = len(command)
unique_command = len(cmd_counter)
average = total_command/unique_command
print(f'Среднее {average}')
for cmd, count in cmd_counter.items():
    if count>average:
        print(f'Комманда {cmd} встречается чаще среднего, а именно {count} раз')
