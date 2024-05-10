
sample_posts = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa."
from flask import render_template,redirect,url_for,flash
from app import app, db
from app.form import PostForm, RegisterForm, LoginForm, CommentForm
from .models import User
from random import randint
from sqlalchemy.exc import IntegrityError

def generate_user_id():
    return '{:06d}'.format(randint(0, 999999))
@app.route('/')
@app.route('/post')
@app.route('/index')
def test():
    form = CommentForm()
    posts = [{'id': 1,
              'community': 'Community 1',
             'topic': 'This is the first topic', 
             'body': sample_posts,
             'author': {'username': "Jake"},
             'time_stamp': '2020-01-01 12:00:00',
             'comments': [{'comment': 'Comment 1', 'comment_body': sample_posts, 'author': {'username': "Jace"}, 'time_stamp': '2020-01-01 12:00:00'},
                {'comment': 'Comment 2', 'comment_body': sample_posts, 'author': {'username': "James"}, 'time_stamp': '2020-01-01 12:00:00'}] 
             },
             {'id': 2,
              'community': 'Community 2',
             'topic': 'This is the second topic', 
             'body': sample_posts,
             'author': {'username': "Jonathon"},
             'time_stamp': '2020-02-01 13:00:00',
             'comments': [{'comment': 'Comment 1', 'comment_body': sample_posts, 'author': {'username': "Kyra"}, 'time_stamp': '2020-02-01 12:00:00'},
                {'comment': 'Comment 2', 'comment_body': sample_posts, 'author': {'username': "Chole"}, 'time_stamp': '2020-02-01 12:00:00'}] 
             }]
    
    return render_template('post.html', title='Home', posts=posts, form=form)


@app.route('/create')
def create():
    form = PostForm()
    return render_template('create_post.html', title='Submit Post', form=form)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    pass

@app.route('/post_comment', methods=['GET', 'POST'])
def post_comment():
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
        try:
            user = User(User_id=generate_user_id(),
                    fname=form.Firstname.data,
                    lname=form.Lastname.data,
                    username=form.Username.data,
                    email=form.email_address.data,
                    password_hash=form.Password.data)
            db.session.add(user)
            db.session.commit()
            flash("You are now registered")
            return redirect(url_for('login'))
        except IntegrityError:
            flash("Registration failed. Please check your input.")
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
