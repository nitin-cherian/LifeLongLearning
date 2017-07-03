# SELECT statement, remove unicode characters


import sqlite3


with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    cursor.execute("SELECT firstname, lastname FROM employees")

    rows_iter = iter(cursor.fetchall())  # fetchall gives a list of tuples

    for firstname, lastname in rows_iter:
        print(firstname, lastname)


