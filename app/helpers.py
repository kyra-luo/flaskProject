# utils.py
from sqlalchemy import select
from app import db
from app.models import Post, Comment, User
import random
import string
from random import randint

def process_posts_with_comments(post_all):
    posts = []
    for post in post_all:
        comment_query = select(Comment).where(Comment.post_id == post.id).order_by(Comment.timestamp.asc())
        posts.append({
            'id': post.id,
            'community': post.community_id,
            'topic': post.topic,
            'body': post.body,
            'author': post.author,
            'timestamp': post.timestamp,
            'comments': db.session.scalars(comment_query).all()
        })
    return posts


def generate_user_id():
    return '{:06d}'.format(randint(0, 999999))

def get_user_posts(user_id):
    query = (
        db.session.query(Post)
        .filter(Post.user_id == user_id)
        .order_by(Post.timestamp.desc())
    )

    posts = query.all()

    results = []
    for post in posts:
        comment_query = (
            db.session.query(Comment, User)
            .join(User, User.id == Comment.user_id)
            .filter(Comment.post_id == post.id)
            .order_by(Comment.timestamp.asc())
        )
        comments = []
        for comment, comment_user in comment_query.all():
            comments.append({
                'comment': comment,
                'commentor': comment_user
            })
        results.append({
            'post': post,
            'comments': comments
        })

    return results


def get_user_comments(user_id):
    query = (
        db.session.query(Comment, Post, User)
        .join(Post, Comment.post_id == Post.id)
        .join(User, Post.user_id == User.id)
        .filter(Comment.user_id == user_id)
        .order_by(Comment.timestamp.asc())
    )

    comments = []
    for comment, post, post_author in query.all():
        comments.append({
            'comment': comment,
            'post': post,
            'post_author': post_author
        })

    return comments

def generate_random_email():
    domains = ["example.com", "test.com", "demo.com"]
    name_length = random.randint(5, 10)
    domain = random.choice(domains)
    
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))
    email = f"{name}@{domain}"
    return email

def generate_random_string(length=5):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=length))
    return random_string