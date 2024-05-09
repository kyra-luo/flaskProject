from flask import render_template,redirect,url_for,flash
from app import app, db
from app.form import PostForm, RegisterForm, LoginForm
from .models import User

@app.route('/')
@app.route('/log')
def index():
    return render_template('post.html', title='Home')


@app.route('/create')
def create():
    form = PostForm()
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
    # if the request method == POST and the form.validate == TRUE.
    if form.validate_on_submit():
        user = User(form.Firstname.data, form.Lastname.data,form.Username.data,
                    form.gender.data,form.Password.data,form.confirm_Password.data,
                    form.email_address.data)
        db.session.add(user)
        flash("You are now registered")
        return redirect(url_for('/login'))
    return render_template('register.html', title='register', form=form)


@app.route('/community', methods=['GET', 'POST'])
def commui():
    return render_template('community.html', title='community')


@app.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('user.html', title='User')


@app.route('/base', methods=['GET', 'POST'])
def base():
    return render_template('base.html', title='base')
