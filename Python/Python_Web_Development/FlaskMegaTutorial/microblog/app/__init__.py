"""
When you import a package, the __init__.py executes and
defines what symbols it exposes to the outside world.
"""
from flask import Flask

app = Flask(__name__)

# from . import routes   # This issame as 'from app import routes'
from app import routes
