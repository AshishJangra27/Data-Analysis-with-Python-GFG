import sqlite3

DB_FILE = 'example.db'
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()


user_name = input('Enter name to search: ')

cursor.execute('SELECT * FROM users WHERE name = ?', (user_name,))

result = cursor.fetchall()
print('Search result:', result)

conn.close()
