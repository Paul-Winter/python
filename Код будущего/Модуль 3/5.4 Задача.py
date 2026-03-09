# Напишите программу, анализирующую хранящиеся в базе данных логи атак с помощью SQL-запросов.
# Она должна вывести в консоль:
#  - Количество атак каждого типа 
#  - Все атаки за последние 24 часа
#  - IP-адресов, с которых было более 5 атак

#### Пояснение к задаче
# Используя модуль sqlite3, подключитесь к базе данных logs_base.db.  В ней находится таблица atak_logs, содержащая  поля:
# id
# type (тип атаки, например, 'SQL-инъекция', 'DDoS' и т.п.)
# datetime (дата и время входа)
# ip (IP-адрес источника атаки)
# Используйте при решении задачи операторы WHERE, HAVING и COUNT.

import sqlite3

# Подключение к базе
connection = sqlite3.connect('logs_base.db')
cursor = connection.cursor()

# 1. Количество атак каждого типа
print("--- Статистика по типам атак ---")
cursor.execute("SELECT type, COUNT(*) FROM atak_logs GROUP BY type")
for row in cursor.fetchall():
    print(f"Тип: {row[0]}, Количество: {row[1]}")

# 2. Все атаки за последние 24 часа
print("\n--- Атаки за последние 24 часа ---")
cursor.execute("SELECT * FROM atak_logs WHERE datetime >= datetime('now', '-1 day')")
for row in cursor.fetchall():
    print(row)

# 3. IP-адреса, с которых было более 5 атак
print("\n--- Подозрительные IP (более 5 атак) ---")
cursor.execute("SELECT ip, COUNT(*) FROM atak_logs GROUP BY ip HAVING COUNT(*) > 5")
for row in cursor.fetchall():
    print(f"IP: {row[0]}, Всего атак: {row[1]}")

connection.close()
