from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'JJmachan'}
    posts = [
            {
                'author': {'username': 'John'},
                'body': 'Learning Flask, Life is beautiful'
            },
            {
                'author': {'username': 'JJmachan'},
                'body': 'This is awesome SHIT!!!'
            },
            ]

    return render_template('index.html', user=user, posts=posts)
