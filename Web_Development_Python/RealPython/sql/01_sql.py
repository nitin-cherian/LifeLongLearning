# Create a SQLite3 database and table


# import the sqlite3 library
import sqlite3


# create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")
conn1 = sqlite3.connect("car.db")


# get a cursor object used to execute SQL commands
cursor = conn.cursor()
cursor1 = conn1.cursor()


# create a table
cursor.execute("""CREATE TABLE IF NOT EXISTS population
                  (city TEXT, state TEXT, population INT)""")
cursor1.execute("""CREATE TABLE IF NOT EXISTS inventory
                   (Make TEXT, Model TEXT, Quantity INT)""")


# close the database connection
conn.close()
conn1.close()
