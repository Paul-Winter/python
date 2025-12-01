# Задача 1
# Простейшая функция мониторинга времени выполнения программы

#   Что делает:
# 1. С помощью модуля datetime записывает время начала.
# 2. Ждёт 2-3 секунды (имитация работы программы).
# 3. Снова фиксирует текущее время.
# 4. Считает разницу во времени (сколько секунд прошло)
# Выводит сообщение: Программа выполнялась 3.002345 секунд
#  - Добавление измерения загруженности процессора и памяти

#   Что делает:
# 1. Импортирует модуль os.
# 2. Использует os.getloadavg() (или аналогичные средства) для получения средней загрузки CPU.
# 3. Если есть доступ, определяет использование памяти (например, через os.popen('free') на Linux).
# 4. Выводит:
# 5. Время выполнения.
# 6. Загрузку CPU.
# 7. Использование памяти.

# Пример вывода:
# python-repl
# Программа выполнялась 3.002345 секунд
# Средняя загрузка CPU: 0.15
# Использование памяти: ...

import datetime
import psutil  # type: ignore
import random
import time

time_start = datetime.datetime.now()
time.sleep(random.randint(2, 3))
time_end = datetime.datetime.now()

time_execute = time_end - time_start
print(f"Программа выполнялась {time_execute} секунд")

proc_load = psutil.cpu_percent()
print(f"Средняя загрузка CPU: {proc_load}%")

print(
    f"Использование памяти: {psutil.virtual_memory().used/1024} MB из {psutil.virtual_memory().total/1024} MB ({psutil.virtual_memory().percent}%)")
