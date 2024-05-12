from flask import render_template, flash, redirect, url_for
from app import app,db
from app.form import PostForm, CommunityForm
import sqlalchemy as sa
from app.models import Community



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
    return render_template('login.html', title='Sign In')

@app.route('/register', methods=['GET', 'POST'])
def regi():
    return render_template('register.html',title='register')

@app.route('/community', methods=['GET', 'POST'])
def community():
    form = CommunityForm()
    if form.validate_on_submit():
        flash('Community created requested for user {}, category={}'.format(form.communityName.data,
            form.category.data))
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
    return render_template('user.html',title='User')
@app.route('/base', methods=['GET', 'POST'])
def base():
    return render_template('base.html',title='base')