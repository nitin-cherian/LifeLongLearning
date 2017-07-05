# hw_01_sql.py

# import sqlite3 library
import sqlite3


with sqlite3.connect('car.db') as connection:
    cursor = connection.cursor()

    records = [
        ('Ford', '2015', 10),
        ('Ford', '2016', 5),
        ('Ford', '2014', 2),
        ('Honda', '2017', 11),
        ('Honda', '2012', 3)
    ]

    cursor.executemany("INSERT INTO inventory VALUES (?, ?, ?)", records)

