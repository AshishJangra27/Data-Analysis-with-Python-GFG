import mysql.connector

# Replace these with your actual MySQL credentials
HOST = 'localhost'         # Host where MySQL server is running
USER = 'root'             # Your MySQL username
PASSWORD = 'gfg@1998' # Your MySQL password
DATABASE = 'myntra' # The database you want to use

# Connect to the MySQL database
conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)
cursor = conn.cursor()


cursor.execute('''
DROP TABLE IF EXISTS users
''')
conn.commit()



# Example: Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
)
''')
conn.commit()



cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
print("All users:", users)



# Example: Insert a user
cursor.execute('''
INSERT INTO users (name, email) VALUES (%s, %s)
''', ("Alice", "alice@example.com"))
conn.commit()




# Example: Query users
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
print("All users:", users)





# Example: Update a user
cursor.execute('''
UPDATE users SET email = %s WHERE name = %s
''', ("alice@newdomain.com", "Alice"))
conn.commit()



cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
print("All users:", users)




# Example: Delete a user
cursor.execute('''
DELETE FROM users WHERE name = %s
''', ("Alice",))
conn.commit()



cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
print("All users:", users)



# Close the connection
conn.close()

# ---
# This script demonstrates basic MySQL operations:
# - Connecting to a database
# - Creating tables
# - Inserting, querying, updating, and deleting records
#
# Change HOST, USER, PASSWORD, and DATABASE to your actual MySQL details.
# For more advanced usage, see the mysql-connector-python documentation:
# https://dev.mysql.com/doc/connector-python/en/
