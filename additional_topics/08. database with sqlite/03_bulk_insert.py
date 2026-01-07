import sqlite3

DB_FILE = 'example.db'
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

users = [
    ("Carol", "carol@example.com"),  # First user
    ("Dave", "dave@example.com"),    # Second user
    ("Eve", "eve@example.com")       # Third user
]


cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', users)
conn.commit()

print('Bulk users inserted successfully.')
conn.close()
