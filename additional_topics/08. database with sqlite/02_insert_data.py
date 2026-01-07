import sqlite3

DB_FILE = 'example.db'
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')")
conn.commit()

print('User inserted successfully.')
conn.close()
