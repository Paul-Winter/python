# Напишите систему логирования для функций, работающих с базой данных. Для этого нужно использовать модуль logging и создать декоратор.Для отладки и мониторинга приложений полезно логировать все SQL-запросы и время их выполнения. Настройте систему логирования с помощью модуля logging.

#### Пояснение к задаче
# 1. Импортируйте  logging и настройте базовую конфигурацию логирования:
#     - Логируем всё, 
#     - Формат сообщений, который мы будем сохранять: (время события, имя логгера, уровень, само сообщение)
#     - Результаты исполнения надо хранить в файле "sql_log.txt"
# 2. Создайте сам логгер, например SQLite
# 3. Напишите функцию для логирования запросов, которая принимает на вход: курсор, запрос и параметры (/None по умолчанию). 
# 4. Эта функция должна
#     - Засекать время начала и окончания и логгирования время выполнения в миллисекундах
#     - Логирровать запрос (и параметры, если есть)
# 5. Подключитесь к тестовой базе (например, test.db), создайте таблицу и выполните запрос через эту функцию.
# 6. Проверьте, что логи появляются в консоли и записываются в файл.

import sqlite3
import logging
import time

# Настройка логгера
logger = logging.getLogger('SQLite')
logger.setLevel(logging.INFO)

# Формат: время, имя, уровень, сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Обработчик для консоли
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)

# Обработчик для файла
file_handler = logging.FileHandler('sql_log.txt', encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def execute_and_log(cursor, query, params=None):
   start = time.perf_counter()
  
   # Выполнение запроса
   if params:
       logger.info(f"Запрос: {query} | Параметры: {params}")
       cursor.execute(query, params)
   else:
       logger.info(f"Запрос: {query}")
       cursor.execute(query)
  
   end = time.perf_counter()
   duration_ms = (end - start) * 1000
   logger.info(f"Время выполнения: {duration_ms:.2f} ms")
  
   return cursor

if __name__ == "__main__":
   conn = sqlite3.connect('test.db')
   curr = conn.cursor()
   execute_and_log(curr, "CREATE TABLE IF NOT EXISTS users (id INT, name TEXT)")
   execute_and_log(curr, "INSERT INTO users VALUES (?, ?)", (1, 'Alice'))
   conn.commit()
   conn.close()
