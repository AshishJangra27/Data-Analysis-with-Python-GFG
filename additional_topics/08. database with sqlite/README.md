# Working with Databases using sqlite3

This folder contains practical Python scripts for working with SQLite databases using the built-in `sqlite3` module. Each script demonstrates a key database operation, from creating tables and inserting data to advanced queries and schema migration. There are also examples for connecting to MySQL databases using `mysql-connector-python`.

## Contents & Topics

1. **01_create_db_and_table.py**
   - Creates a SQLite database file and a `users` table with id, name, and email fields.
   - Demonstrates connecting, creating tables, and closing connections.

2. **02_insert_data.py**
   - Inserts a single user (Bob) into the `users` table.
   - Shows how to execute insert statements and commit changes.

3. **03_bulk_insert.py**
   - Inserts multiple users (Carol, Dave, Eve) at once using `executemany`.
   - Efficient for adding many records in one go with parameterized queries.

4. **04_query_data.py**
   - Fetches and prints all users from the table using `fetchall()`.
   - Demonstrates querying and iterating over results.

5. **05_update_data.py**
   - Updates Bob's email address to bob@hotmail.com.
   - Shows how to execute update statements and commit changes.

6. **06_delete_data.py**
   - Deletes Bob from the users table.
   - Demonstrates executing delete statements and committing changes.

7. **07_parameterized_queries.py**
   - Uses parameterized queries to prevent SQL injection.
   - Safely searches for users by name using user input with `?` placeholders.

8. **08_alter_table.py**
   - Demonstrates schema migration by adding an `age` column to the table.
   - Shows how to alter table structure safely using `ALTER TABLE`.

9. **09_connecting_with_existing_databases.py**
   - Connects to a MySQL database using `mysql-connector-python`.
   - Demonstrates creating tables, inserting, querying, updating, and deleting records in MySQL.
   - Update HOST, USER, PASSWORD, and DATABASE variables for your own MySQL setup.

## How to Use
- Run each script individually to learn and practice specific database operations:

```bash
python "07. database with sqlite/01_create_db_and_table.py"
python "07. database with sqlite/02_insert_data.py"
python "07. database with sqlite/04_query_data.py"
```

- Scripts are self-contained and can be modified for your own data and schema.
- For MySQL examples (script 09), install `mysql-connector-python` and update credentials.

## Learning Path Recommendation
1. Start with `01_create_db_and_table.py` to create your database.
2. Use `02_insert_data.py` and `03_bulk_insert.py` to add data.
3. Query with `04_query_data.py` and update/delete with `05_update_data.py` and `06_delete_data.py`.
4. Learn SQL injection prevention with `07_parameterized_queries.py`.
5. Understand schema changes with `08_alter_table.py`.
6. Explore MySQL integration with `09_connecting_with_existing_databases.py`.

## Requirements
- Python 3.x
- No external packages needed for SQLite examples (uses built-in `sqlite3`).
- For MySQL examples:
  ```sh
  pip install mysql-connector-python
  ```

## Learning Resources
- [Python sqlite3 documentation](https://docs.python.org/3/library/sqlite3.html)
- [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/)

## License
This folder is for educational purposes. Feel free to use, modify, and share the code.
