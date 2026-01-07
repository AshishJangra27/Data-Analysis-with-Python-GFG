import sqlite3

DB_FILE = 'example.db'
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute('SELECT * FROM users')

users = cursor.fetchall()

for user in users:
    print(user)

conn.close()
