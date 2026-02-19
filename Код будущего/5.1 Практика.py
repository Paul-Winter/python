import sqlite3

conn = sqlite3.connect("db.test")
cursor = conn.cursor()

# name = input("Введите имя: ")
cursor.execute("""
               CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               role TEXT,
               login_time TEXT
               )
               """)
# cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
# cursor.execute("""INSERT INTO users (name, role, login_time)
#                VALUES
#                ("Alice", "admin", "2025-06-13 10:23"),
#                ("Bob", "user", "2025-06-13 11:02"),
#                ("Mallory", "attacker", "2025-06-13 11:06")""")
cursor.execute("SELECT name FROM users WHERE role = 'admin'")
admins = cursor.fetchall()
cursor.execute("SELECT name FROM users WHERE role = 'user'")
users = cursor.fetchall()
cursor.execute("SELECT name FROM users WHERE role = 'attacker'")
attackers = cursor.fetchall()
print(admins)
print(users)
print(attackers)