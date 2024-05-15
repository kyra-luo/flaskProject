from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import current_user, login_required, login_user, logout_user
from urllib.parse import urlsplit
from app import app, db
from app.form import PostForm, RegisterForm, LoginForm, CommentForm, CommunityForm
import sqlalchemy as sa
from app.models import User, Post, Community, Comment
from random import randint
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

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
    
    post_all=db.session.scalars(query).all()
    if post_all is None:
        return redirect(url_for('create'))
    else:
        posts =[]
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
        post = Post(body=form.body.data,topic=form.topic.data, author=current_user)
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
def community():
    form = CommunityForm()
    if form.validate_on_submit():
        try:
            community = Community(
                    communityName=form.communityName.data,
                    category=form.category.data,
                    description=form.description.data
                    )
            db.session.add(community)
            db.session.commit()
            flash('Community {} created, category={}'.format(form.communityName.data,
            form.category.data))
        except IntegrityError:
            flash("Registration failed. Please check your input.")
        return redirect(url_for('community'))
    return render_template('community.html',title='community', form=form)

@app.route('/community/<category>', methods=['GET', 'POST'])
def cate(category):
    forums = db.first_or_404(sa.select(Community).where(Community.category == category))
    subforums = [ {'name': forums, 'description': forums }  ] # or don't need this line
    form = CommunityForm()
    if form.validate_on_submit():

        flash('Community created requested for user {}, category={}'.format(form.communityame.data,
            form.category.data))
        return redirect(url_for('community'))
    return render_template('community.html',title='community', forums=forums, subforums=subforums, form=form)

@app.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('user.html', title='User')


@app.route('/base', methods=['GET', 'POST'])
def base():
    return render_template('base.html', title='base')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
