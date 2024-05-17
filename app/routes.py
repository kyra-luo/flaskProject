from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import current_user, login_required, login_user, logout_user
from urllib.parse import urlsplit
from app import app, db
from app.form import PostForm, RegisterForm, LoginForm, CommentForm, UserForm
import sqlalchemy as sa
from app.models import User, Post, Comment
from random import randint
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()

sample_posts = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa."


def generate_user_id():
    return '{:06d}'.format(randint(0, 999999))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/explore', methods=['GET', 'POST'])
@login_required
def test():
    form = CommentForm()
    query = sa.select(Post).order_by(Post.timestamp.desc())
    
    post_all = db.session.scalars(query).all()
    if post_all is None:
        return redirect(url_for('create'))
    else:
        posts = []
        for post in post_all:
            comment_query = sa.select(Comment).where(Comment.post_id == post.id).order_by(Comment.timestamp.asc())
            posts.append({
                'id': post.id,
                'community': 'Community 1',
                'topic': post.topic,
                'body': post.body,
                'author': post.author,
                'time_stamp': post.timestamp,
                'comments': db.session.scalars(comment_query).all()
            })
        
    return render_template('post.html', title='Home', posts=posts, form=form)


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, topic=form.topic.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
    return render_template('create_post.html', title='Create Post', form=form)


@app.route('/post_comment', methods=['POST'])
@login_required
def post_comment():
    if request.method == 'POST':
        form = CommentForm()        
        if form.validate_on_submit():
            post_id = form.post_id.data
            current_post = db.session.scalar(sa.select(Post).where(Post.id == int(post_id)))
            comment = Comment(comment=form.comment_body.data, underPost=current_post, commentor=current_user)
            db.session.add(comment)
            db.session.commit()
            flash('Your comment is now live!')
            comment_html = render_template('_comment.html', comment=comment)
            print(comment_html)
            return jsonify({'comment_html': comment_html})
    
    return jsonify({'error': 'Invalid data'}), 400


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('base'))
    form = LoginForm()
    if form.validate_on_submit():
        print('Form data received:', form.email_addr.data, form.password.data)

        user = db.session.scalar(
            sa.select(User).where(User.email == form.email_addr.data))
        print('User found:', user)  # Add this line to check if user is retrieved

        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            print('Invalid email or password')  # Add this line to check if this condition is met
            return redirect(url_for('login'))

        login_user(user)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        print(current_user.is_authenticated)
        return redirect(url_for('base'))  # Redirect to index page
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
                        password_hash=generate_password_hash(form.Password.data, method='pbkdf2:sha256'))
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


def get_user_posts(user_id):
    # 获取用户的所有帖子和每个帖子的评论
    query = (
        db.session.query(Post, Comment, User)
        .join(Comment, Post.id == Comment.post_id)
        .join(User, User.id == Comment.user_id)
        .filter(Post.user_id == user_id)
        .order_by(Post.timestamp.desc(), Comment.timestamp.asc())
    )

    results = query.all()

    # 组织数据
    posts = {}
    for post, comment, comment_user in results:
        if post.id not in posts:
            posts[post.id] = {
                'post': post,
                'comments': []
            }
        posts[post.id]['comments'].append({
            'comment': comment,
            'commentor': comment_user
        })

    return posts

def get_user_comments(user_id):
    # 获取用户的所有评论及其相关的帖子信息
    query = (
        db.session.query(Comment, Post, User)
        .join(Post, Comment.post_id == Post.id)
        .join(User, Post.user_id == User.id)
        .filter(Comment.user_id == user_id)
        .order_by(Comment.timestamp.asc())
    )

    results = query.all()

    comments = []
    for comment, post, post_author in results:
        comments.append({
            'comment': comment,
            'post': post,
            'post_author': post_author
        })

    return comments



@app.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    # 获取指定用户名的用户信息
    user = db.session.query(User).filter_by(username=username).first_or_404()
    if not user:
        abort(404)

    # 获取用户的帖子及其评论
    posts = get_user_posts(user.id)
    post_count = len(posts)

    # 获取用户的评论及其相关帖子信息
    comments = get_user_comments(user.id)
    comment_count = len(comments)

    form = CommentForm()
    userform = UserForm()

    if userform.validate_on_submit():
        try:
            user.username = userform.username.data
            user.about_me = userform.about_me.data
            db.session.commit()
            flash('Profile updated successfully!', 'success')
            return redirect(url_for('user', username=user.username))
        except Exception as e:
            db.session.rollback()
            flash('Error updating profile: ' + str(e), 'error')
    elif request.method == 'GET':
        userform.username.data = user.username
        userform.about_me.data = user.about_me

    return render_template('user.html', title='User Profile', user=user, form=form, userform=userform, posts=posts, comments=comments, post_count=post_count, comment_count=comment_count)
@app.route('/base', methods=['GET', 'POST'])
def base():
    return render_template('base.html', title='base')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
