from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


# The code in the below comment works. Added for understanding.
# from app import routes
# print(routes.index())
# from app import Flask
# print(Flask.__doc__)
