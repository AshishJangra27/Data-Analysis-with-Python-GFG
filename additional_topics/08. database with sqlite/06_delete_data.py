import sqlite3

DB_FILE = 'example.db'
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute('DELETE FROM users WHERE name = "Bob"')
conn.commit()

print('User deleted successfully.')
conn.close()
