from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required, login_user, logout_user
from app import app, db
from app.form import PostForm, UserForm
import sqlalchemy as sa
from app.models import User
from random import randint
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
@app.route('/log')
def index():
    user = {'username': 'Miguel'}
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

@app.route('/community', methods=['GET', 'POST'])
def commui():
    return render_template('community.html',title='community')



@app.route('/user', methods=['GET', 'POST'])
#@login_required
def user():
    user = current_user
    form = UserForm()
    if form.validate_on_submit():
        try:
            # 创建新用户或更新现有用户
            user = User(name=form.name.data,
                about_me=form.about_me.data,
                community_id=form.Communities.data
            )
            db.session.add(user)
            db.session.commit()
            flash('Profile updated successfully!', 'success')
        except Exception as e:
            db.session.rollback()  # 发生错误时回滚
            flash('Error updating profile: ' + str(e), 'error')
    return render_template('user.html', title='User', form=form)

@app.route('/user/<username>/posts')
def user_posts(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)
@app.route('/user/<username>/comments')
def user_comments(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    comments = [
        {'author': user, 'body': 'Test comments #1'},
        {'author': user, 'body': 'Test comments #2'}
    ]
    return render_template('user.html', user=user, posts=comments)

@app.route('/base', methods=['GET', 'POST'])
def base():
    return render_template('base.html',title='base')