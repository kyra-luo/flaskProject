import unittest
from werkzeug.security import generate_password_hash, check_password_hash

from config import TestingConfig
from app import create_app, db
from app.models import User, Post, Comment

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_hash_password(self):
        p = generate_password_hash('cat')
        u = User(username='susan', fname='Susan', lname='Smith', email='like@qq.com', password_hash=p)
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

# please run the following command to run the test
# python -m unittest tests.unit_test

