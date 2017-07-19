# blog.py - controller


# imports
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
import sqlite3


# configuration
DATABASE = "blog.db"


# Create an instance of Flask class
app = Flask(__name__)


# pulls in app configurations by looking for UPPERCASE variables
app.config.from_object(__name__)


# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


if __name__ == '__main__':
    app.run(debug=True)


