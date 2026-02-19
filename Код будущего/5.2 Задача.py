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