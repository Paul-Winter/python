# Напишите программу, которая работает с таблицей пользователей в базе данных, используя модуль sqlite3.
# Нужно вывести список всех пользователей, потом добавить нового пользователя “Анна” с текущей датой регистрации,
# а затем вывести из базы только тех пользователей, которые зарегистрированы после 1 января 2023 года.

#### Пояснение к задаче
# Используя модуль sqlite3, подключитесь к базе данных users_base.db.
# В ней в таблице users (правилом хорошего тона является называть таблицы латинскими буквами,
# т.к. не все системы одинаково работают с таблицами,
# названия которых содержат иные символы) содержится информация о пользователях:
# id (уникальный идентификатор)
# name (имя пользователя)
# email (электронная почта)
# registration_date (дата регистрации)

# С помощью SQL-запросов:
# Выведите имена, адреса и даты регистрации всех пользователей
# Добавьте нового пользователя с именем "Анна", email "anna@example.com" и текущей датой регистрации.
# Найдите и выведите id, имена и дату регистрации для всех пользователей, зарегистрированных после 1 января 2023 года.

import sqlite3
from datetime import datetime

conn = sqlite3.connect('users_base.db')
cursor = conn.cursor()

# 1. Вывод всех пользователей
cursor.execute("SELECT name, email, registration_date FROM users")
for user in cursor.fetchall():
    print(f"Имя: {user[0]}, Email: {user[1]}, Дата: {user[2]}")

# 2. Добавления нового пользователя с именем "Анна", email "anna@example.com" и текущей датой регистрации
today = datetime.now().strftime("%Y-%m-%d")
cursor.execute("INSERT INTO users (name, email, registration_date) VALUES (?, ?, ?)", "Анна", "anna@example.com", today)

# 3. Поиск пользователей, зарегистрированных после 1 января 2023 года
cursor.execute("SELECT id, name, registration_date FROM users WHERE registration_date > '2023-01-01'")
for user in cursor.fetchall():
    print(f"ID: {user[0]}, Имя: {user[1]}, Дата: {user[2]}")

conn.close()
