from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import current_user, login_required, login_user, logout_user
from urllib.parse import urlsplit
from app import app, db
from app.form import PostForm, RegisterForm, LoginForm, CommentForm, ResetPasswordRequestForm, ResetPasswordForm, CommunityForm
import sqlalchemy as sa
from app.models import User, Post, Community, Comment
from random import randint
from sqlalchemy.exc import IntegrityError
from app.blueprint import main
from werkzeug.security import generate_password_hash, check_password_hash
from app.email import send_password_reset_email, send_welcome_email
from app.helpers import process_posts_with_comments

sample_posts = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa."


def generate_user_id():
    return '{:06d}'.format(randint(0, 999999))

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', title='Home')

@main.route('/explore', methods=['GET', 'POST'])
@login_required
def test():
    comment_form = CommentForm()
    query = sa.select(Post).order_by(Post.timestamp.desc())
    post_all=db.session.scalars(query).all()
    communities = db.session.query(Community).all()
    if post_all is None:
        return redirect(url_for('main.create'))
    elif communities is None:
        return redirect(url_for('community'))
    else:
        posts = process_posts_with_comments(post_all)
    return render_template('post.html', title='Home', posts=posts, comment_form=comment_form)


@main.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    community_list = db.session.query(Community).all()
    if community_list is None:
        community_choices = []
    else:
        community_choices = [(str(community.id), community.communityName) for community in community_list]
    form.communities.choices = [('', 'Select a community...')] + community_choices
    if form.validate_on_submit():
        community_id = form.communities.data
        current_community = db.session.scalar(sa.select(Community).where(Community.id == int(community_id)))
        post = Post(body=form.body.data,topic=form.topic.data, community=current_community, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
    return render_template('create_post.html', title='Create Post', form=form)


@main.route('/post_comment', methods=['POST'])
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
            return jsonify({'comment_html': comment_html})
    
    return jsonify({'error': 'Invalid data'}), 400

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.base'))
    form = LoginForm()
    if form.validate_on_submit():
        print('Form data received:', form.email_addr.data, form.password.data)

        user = db.session.scalar(
            sa.select(User).where(User.email == form.email_addr.data))
        print('User found:', user)  # Add this line to check if user is retrieved

        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            print('Invalid email or password')  # Add this line to check if this condition is met
            return redirect(url_for('main.login'))

        login_user(user)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
        print(current_user.is_authenticated)
        return redirect(url_for('main.base'))  # Redirect to index page
    return render_template('login.html', title='Sign In', form=form)


@main.route('/register', methods=['GET', 'POST'])
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
            send_welcome_email(user)
            flash("You are now registered")
            return redirect(url_for('main.login'))
        except IntegrityError:
            flash("Registration failed. Please check your input.")
    return render_template('register.html', title='register', form=form)

@main.route('/community', defaults={'category': None}, methods=['GET', 'POST'])
@main.route('/community/<category>', methods=['GET', 'POST'])
def community(category):
        if category:
            forums = db.session.query(Community).filter_by(category=category).all()
        else:
            forums = db.session.query(Community).all()
        comment_form = CommentForm()
        community_form = CommunityForm()
        if community_form.validate_on_submit():
            community = Community(
                    communityName=community_form.communityName.data,
                    category=community_form.category.data,
                    description=community_form.description.data
                    )
            db.session.add(community)
            db.session.commit()
            flash('Community created requested for user {}, category={}'.format(community_form.communityName.data, community_form.category.data))
            return redirect(url_for('community'))
        return render_template('community.html',title='community', comment_form=comment_form, forums=forums, community_form=community_form)

@main.route('/community/<category>/<id>', methods=['GET', 'POST'])
def forum(category, id):
    if category and id:
        comment_form = CommentForm()
        community_form = CommunityForm()
        query = sa.select(Post).where(Post.community_id == id
        ).order_by(Post.timestamp.desc())
        post_all=db.session.scalars(query).all()
        communities = db.session.query(Community).all()
        if post_all is None:
            return redirect(url_for('main.create'))
        elif communities is None:
            return redirect(url_for('community'))
        else:
            posts = process_posts_with_comments(post_all)
        return render_template('forum.html', title='Home', posts=posts, comment_form=comment_form, community_form=community_form)


# @main.route('/community', defaults={'category': None, 'id': None}, methods=['GET', 'POST'])
# @main.route('/community/<category>', defaults={'id': None}, methods=['GET', 'POST'])
# @main.route('/community/<category>/<id>', methods=['GET', 'POST'])
# def community(category, id):
#         posts = []
#         if category:
#             forums = db.session.query(Community).filter_by(category=category).all()
#             if id:
#                 query = sa.select(Post).where(Post.community_id == id
#                 ).order_by(Post.timestamp.desc())
#                 post_all=db.session.scalars(query).all()
#                 posts = process_posts_with_comments(post_all)
#         else:
#             forums = db.session.query(Community).all()      
#         comment_form = CommentForm()
#         community_form = CommunityForm()
#         if community_form.validate_on_submit():
#             community = Community(
#                     communityName=community_form.communityName.data,
#                     category=community_form.category.data,
#                     description=community_form.description.data
#                     )
#             db.session.add(community)
#             db.session.commit()
#             flash('Community created requested for user {}, category={}'.format(community_form.communityName.data, community_form.category.data))
#             return redirect(url_for('community'))
#         return render_template('community.html',title='community', comment_form=comment_form, forums=forums, community_form=community_form, posts=posts)
@main.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('user.html', title='User')


@main.route('/base', methods=['GET', 'POST'])
def base():
    return render_template('base.html', title='base')

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('mian.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.email == form.email.data))
        if user:
            send_password_reset_email(user)  # 修改这里，不再需要传递 form 参数
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('main.login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        print("11111")
        user.set_password(form.password.data)
        db.session.commit()
        print("1111111")
        flash('Your password has been reset.')
        return redirect(url_for('mian.login'))
    return render_template('reset_password.html', form=form)
