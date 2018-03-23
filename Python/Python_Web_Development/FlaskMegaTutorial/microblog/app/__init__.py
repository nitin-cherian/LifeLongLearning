"""
When you import a package, the __init__.py executes and
defines what symbols it exposes to the outside world.
"""
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)  # represents the database
migrate = Migrate(app, db)  # represents the migration engine
login = LoginManager(app)   # manages user logins
login.login_view = 'login'

# from . import routes   # This is same as 'from app import routes'
from app import routes, models
