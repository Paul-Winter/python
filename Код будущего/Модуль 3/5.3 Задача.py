# Напишите программу, которая в существующей базе данных создает новую таблицу IB_issues со следующими полями:
# id (целое число, первичный ключ)
# описание (текст)
# дата (дата)
# статус (текст: 'открыт', 'в работе', 'закрыт')

#### Пояснение к задаче
# Используя модуль sqlite3, подключитесь к базе данных logs_base.db, в котором создайте требуемую таблицу, используя оператор CREATE TABLE.

import sqlite3

# Подключаемся к существующей базе данных
connection = sqlite3.connect('logs_base.db')
cursor = connection.cursor()

# Создание новой таблицы IB_issues
# Используем AUTOINCREMENT для id, чтобы он заполнялся автоматически
cursor.execute('''
CREATE TABLE IF NOT EXISTS IB_issues (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   describe TEXT NOT NULL,
   datatime DATETIME NOT NULL,
   status TEXT NOT NULL
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

print("Таблица IB_issues успешно создана.")
