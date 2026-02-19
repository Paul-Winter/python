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