# hw_02_sql.py

# import sqlite3 library
import sqlite3


with sqlite3.connect('car.db') as connection:
    cursor = connection.cursor()

    cursor.execute("UPDATE inventory SET quantity=6 WHERE make='Ford' and model='2016'")
    cursor.execute("UPDATE inventory SET quantity=4 WHERE make='Honda' and model='2012'")

    print("NEW DATA:\n\n")
    cursor.execute("SELECT * from inventory")

    for row in cursor.fetchall():
        print(row[0], row[1], row[2])



