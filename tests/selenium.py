
import multiprocessing
import time
from unittest import TestCase 
from selenium import webdriver  
from app import create_app, db
from config import SeleniumConfig, TestingConfig
from app.models import User, Post, Comment

localHost = "http://localhost:5000/"

class SeleniumTestCase(TestCase):

    def setUp(self):
        self.testApp = create_app(SeleniumConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()

        multiprocessing.set_start_method('fork')
        self.server_process = multiprocessing.Process(target=self.testApp.run)
        self.server_process.start()
    
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(localHost)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

        self.server_process.terminate()
        self.driver.close()


    def test_login_page(self):
        time.sleep(5)
        self.assertTrue(True)

        # loginElement = self.driver.find_element(By.ID, "login")
        # loginElement.send_keys("01349324")