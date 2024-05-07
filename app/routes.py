from flask import render_template
from app import app
from app.form import PostForm, CommentForm

sample_posts = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore quod aliquid asperiores modi sequi minus nostrum porro sint! Quasi molestiae necessitatibus accusamus nisi libero repudiandae, eum pariatur unde eveniet culpa."

@app.route('/')
@app.route('/post')
@app.route('/index')
def index():
    posts = {'topic': 'Topic', 
             'body': sample_posts,
             'author': 'Jake',
             'time_stamp': '2020-01-01 12:00:00' 
             }
    comments = [{'comment': 'Comment 1', 'comment_body': sample_posts, 'author': 'Jace', 'time_stamp': '2020-01-01 12:00:00'},
                {'comment': 'Comment 2', 'comment_body': sample_posts, 'author': 'James', 'time_stamp': '2020-01-01 12:00:00'}]
    return render_template('post.html', title='Home', posts=posts, comments=comments)

@app.route('/test')
def test():
    form = CommentForm()
    posts = {'topic': 'Topic', 
             'body': sample_posts,
             'author': 'Jake',
             'time_stamp': '2020-01-01 12:00:00' 
             }
    comments = [{'comment': 'Comment 1', 'comment_body': sample_posts, 'author': 'Jace', 'time_stamp': '2020-01-01 12:00:00'},
                {'comment': 'Comment 2', 'comment_body': sample_posts, 'author': 'James', 'time_stamp': '2020-01-01 12:00:00'}]
    return render_template('test.html', title='Home', posts=posts, comments=comments, form=form)

@app.route('/create')
def create():
    form=PostForm()
    return render_template('create_post.html', title='Submit Post', form=form)

@app.route('/submit', methods=['GET', 'POST'])
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
def user():
    return render_template('user.html',title='User')
@app.route('/base', methods=['GET', 'POST'])
def base():
    return render_template('base.html',title='base')