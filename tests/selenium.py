
import multiprocessing
import time
from unittest import TestCase 
from selenium import webdriver  
from app import create_app, db
from config import SeleniumConfig, TestingConfig
from selenium.webdriver.common.by import By
from app.models import User, Post, Comment
from werkzeug.security import generate_password_hash, check_password_hash

localHost = "http://localhost:5000/"

class SeleniumTestCase(TestCase):

    def setUp(self):
        self.testApp = create_app(SeleniumConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()
        p = generate_password_hash('cat')
        u = User(username='susan', fname='Susan', lname='Smith', email='like@qq.com', password_hash=p)

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


    def test_register_button(self):
        # Find the button using its text or other attribute
        button = self.driver.find_element(By.XPATH, "//button[text()='Get account']")
        button.click()
        
        # Allow some time for the navigation
        time.sleep(2)

        # Verify the URL
        current_url = self.driver.current_url
        expected_url = localHost + "register"
        self.assertEqual(current_url, expected_url)
