from flask import render_template
from app import app
from app.form import PostForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('post.html', title='Home')

@app.route('/create')
def create():
    form=PostForm()
    return render_template('create_post.html', title='Submit Post', form=form)

@app.route('/submit', methods=['GET'])
def submit():
    pass
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Sign In')

@app.route('/register', methods=['GET', 'POST'])
def regi():
    return render_template('register.html',title='register')

@app.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('user.html',title='User')