from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nitin'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {

            'author': {'username': 'Aeben'},
            'body': 'My favorite cartoon is "Paw Patrol"'
        },
        {

            'author': {'username': 'Sneha'},
            'body': 'I work at Infosys'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
