import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')


def add_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(8659746, '2017-06-08', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()


create_table()
add_entry()

