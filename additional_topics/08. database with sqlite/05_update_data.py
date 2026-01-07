import sqlite3

DB_FILE = 'example.db'
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute('UPDATE users SET email = "bob@hotmail.com" WHERE name = "Bob"')

conn.commit()

print('User updated successfully.')
conn.close()
