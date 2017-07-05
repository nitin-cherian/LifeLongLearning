# hw_03_sql.py


# import sqlite3 library
import sqlite3


connection = sqlite3.connect('car.db')
cursor = connection.cursor()

cursor.execute("SELECT * from inventory WHERE make='Ford'")

for row in cursor.fetchall():
    print(row[0], row[1], row[2])

connection.close()
