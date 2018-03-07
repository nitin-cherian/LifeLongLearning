"""
When you import a package, the __init__.py executes and
defines what symbols it exposes to the outside world.
"""
from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# from . import routes   # This is same as 'from app import routes'
from app import routes
