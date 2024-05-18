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