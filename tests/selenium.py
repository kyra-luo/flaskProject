
import multiprocessing
import time
from unittest import TestCase 
from selenium import webdriver  
from app import create_app, db
from config import TestingConfig
from app.models import User, Post, Comment

localHost = 'http://localhost:5000'

class SeleniumTestCase(TestCase):

    def setUp(self):
        self.test_app = create_app(TestingConfig)
        self.app_context = self.test_app.app_context()
        self.app_context.push()
        db.create_all()

        self.server_process = multiprocessing.Process(target=self.test_app.run)
        self.server_process.start()
        self.browser = webdriver.Chrome()
        self.driver.get(localHost) 

    def tearDown(self):
        db.session
        db.drop_all()
        self.app_context.pop()

        self.server_process.terminate()
        self.driver.close()

    def test_login(self):
        time.sleep(100)
        self.assertTrue(True)