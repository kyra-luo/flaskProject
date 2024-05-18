# utils.py
from sqlalchemy import select
from app import db
from app.models import Post, Comment
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