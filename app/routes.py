from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
