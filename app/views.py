from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    books = [
        {
            'title': 'Where is my money?',
            'authors': [{ 'name': 'John Dou' }],
            'year': 1998
        },
        {
            'title': 'Big Ice brick: Part 1',
            'authors': [{ 'name': 'Gill Samuel' }],
            'year': 1999
        },
        {
            'title': 'Big Ice brick: Part 2',
            'authors': [{ 'name': 'Gill Samuel' }, { 'name': 'Peret Samuel' }],
            'year': 1999
        },
        {
            'title': 'Here is I',
            'authors': [{ 'name': 'Kelly Perry' }, { 'name': 'John Dou' }],
            'year': 2001
        },
    ]
    return render_template("index.html", books=books)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Sign In', form = form)
