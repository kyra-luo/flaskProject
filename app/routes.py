from flask import render_template
from app import app
from app.form import PostForm, RegisterForm,LoginForm

@app.route('/')
@app.route('/log')
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
    form = LoginForm()  # 创建登录表单的实例
    if form.validate_on_submit():
        # 执行登录逻辑
        pass
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def regi():
    form = RegisterForm()
    if form.validate_on_submit():
        # add some conditions
        pass
    return render_template('register.html', title='register', form=form)


@app.route('/community', methods=['GET', 'POST'])
def commui():
    return render_template('community.html',title='community')

@app.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('user.html',title='User')
@app.route('/base', methods=['GET', 'POST'])
def base():
    return render_template('base.html',title='base')