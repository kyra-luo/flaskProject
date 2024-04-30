
from flask import render_template
from app import app
from app.form import PostForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('post.html', title='Home')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form=PostForm()
    return render_template('create_post.html', title='Submit Post', form=form)