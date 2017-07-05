# UPDATE and DELETE statements


# import sqlite3 library
import sqlite3


with sqlite3.connect('new.db') as connection:
    cursor = connection.cursor()

    # Update table
    cursor.execute("UPDATE population SET population=9000000 WHERE city='New York City'")

    # Delete data
    cursor.execute("DELETE FROM population WHERE city='Boston'")

    # Select all the data
    cursor.execute("SELECT * from population")

    print('NEW DATA:\n\n')

    for row in cursor.fetchall():
        print(row[0], row[1], row[2])

