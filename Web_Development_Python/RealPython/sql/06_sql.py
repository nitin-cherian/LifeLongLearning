# SELECT statement


# import sqlite3 library
import sqlite3


with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    # use a for loop to iterate through the database, printing the result line by line
    for row in cursor.execute("SELECT firstname, lastname FROM employees"):
        print(row)
