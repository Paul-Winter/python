# Напишите программу, с помощью SQL-запросов извлекающая и выводящих на экран из логов входа в некоторую информационную систему, хранящихся в базе данных:
# все входы, в систему, осуществленные с IP-адреса 192.168.1.1. 
# входы в систему, которые произошли вчера.
# входы пользователя с user_id = 5 за последние 7 дней

#### Пояснение к задаче
# Используя модуль sqlite3, подключитесь к базе данных logs_base.db.
# В ней находится таблица login_logs, содержащая  поля:
# id
# user_id (идентификатор пользователя)
# datetime (дата и время входа)
# ip (IP-адрес)
# Используйте оператор WHERE для получения только нужной информации.

import sqlite3

conn = sqlite3.connect("logs_base.db")
cursor = conn.cursor()

# 1. Поиск всех входов с IP-адреса 192.168.1.1
cursor.execute("""SELECT * FROM login_logs
                  WHERE ip = '192.168.1.1'
               """)
for row in cursor.fetchall():
    print(row)

# 2. Поиск входов, которые произошли вчера
cursor.execute("""SELECT * FROM login_logs
                  WHERE date(datetime) = date('now', '-1 day')
               """)
for row in cursor.fetchall():
    print(row)

# 3. Поиск входов пользователя с user_id = 5 за последние 7 дней
cursor.execute("""SELECT * FROM login_logs
                  WHERE user_id = 5 AND
                  datetime >= datetime('now', '-7 days')
               """)
for row in cursor.fetchall():
    print(row)

conn.close()
