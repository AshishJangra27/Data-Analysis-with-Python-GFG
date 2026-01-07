import sqlite3

DB_FILE = 'example.db'
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute('ALTER TABLE users ADD COLUMN age INTEGER')
conn.commit()

print('Schema migration completed. Column "age" added.')
conn.close()
