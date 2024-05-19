import unittest
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select
import sqlalchemy as sa
from config import TestingConfig
from app import create_app, db
from app.models import User, Post, Comment, Community
from app.helpers import generate_user_id, generate_random_email, generate_random_string, process_posts_with_comments

user_id = generate_user_id()

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.addCleanup(self.cleanup)

    def cleanup(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def create_user(self, username='susan', user_id=None, fname='Susan', lname='Smith', email='like@qq.com', password='cat'):
        if not user_id:
            user_id = generate_user_id()
        p = generate_password_hash(password)
        u = User(username=username, User_id=user_id, fname=fname, lname=lname, email=email, password_hash=p)
        db.session.add(u)
        db.session.commit()
        return u

    def create_community(self):
        c = Community(communityName="Test Community", category="Sport", description="This is a test community")
        db.session.add(c)
        db.session.commit()
        return c

    def create_post(self):
        community_first = db.session.query(Community).first()
        author_first = db.session.query(User).first()
        p = Post(topic="Test Post", body="This is a test post", community=community_first, author=author_first)
        db.session.add(p)
        db.session.commit()
        return p

    def create_comment(self):
        post_first = db.session.query(Post).first()
        author_first = db.session.query(User).first()
        c = Comment(comment="This is a test comment", underPost=post_first, commentor=author_first)
        db.session.add(c)
        db.session.commit()
        return c

    # def test_hash_password(self):
    #     p = generate_password_hash('cat')
    #     u = User(username='susan', User_id = user_id, fname='Susan', lname='Smith', email='like@qq.com', password_hash=p)
    #     self.assertFalse(u.check_password('dog'))
    #     self.assertTrue(u.check_password('cat'))

    def test_comments(self):
        self.create_user()
        self.create_community()
        self.create_post()
        self.create_comment()
        query = sa.select(Post).order_by(Post.timestamp.desc())
        post_all=db.session.scalars(query).all()
        post = process_posts_with_comments(post_all)
        self.assertEqual(len(post[0]['comments']), 1)


    

# please run the following command to run the test
# python -m unittest tests.unit_test

