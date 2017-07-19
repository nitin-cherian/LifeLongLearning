# sql.py - Create a sqlite3 table and populate it with data


# import sqlite3 library
import sqlite3


# create a new database if the database already does not exist
with sqlite3.connect("blog.db") as connection:

    # get a cursor object to execute sql commands
    c = connection.cursor()

    # create the table
    c.execute("CREATE TABLE posts(title TEXT, post TEXT)")

    # insert dummy data into the table
    c.execute('INSERT INTO posts VALUES("Good", "I\'am good")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'am well")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'am excellent")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'am good")')


