
import multiprocessing
import time
from unittest import TestCase 
from selenium import webdriver  
from app import create_app, db
from config import SeleniumConfig, TestingConfig
from selenium.webdriver.common.by import By
from app.models import User, Post, Comment, Community
from werkzeug.security import generate_password_hash, check_password_hash
from app.helpers import generate_user_id

localHost = "http://localhost:8000/"

if not multiprocessing.get_start_method(allow_none=True):
    multiprocessing.set_start_method('fork')

Uid=generate_user_id()

class SeleniumTestCase(TestCase):

    def setUp(self):
        self.testApp = create_app(SeleniumConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()
       

        self.server_process = multiprocessing.Process(target=self.testApp.run, kwargs={'port': 8000})
        self.server_process.start()
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(localHost)

    def tearDown(self):
        self.driver.close()
        self.server_process.terminate()
        self.server_process.join()

        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def create_test_user(self):
        p = generate_password_hash('cat')
        u = User(username='susan', User_id=Uid, fname='Susan', lname='Smith', email='like@outlook.com', password_hash=p)
        db.session.add(u)
        db.session.commit()


    def actual_login(self):
        self.create_test_user()
        time.sleep(2)
        email_addr="like@outlook.com"
        pin="cat"
        button = self.driver.find_element(By.XPATH, "//button[text()='Log In']")
        button.click()
        email = self.driver.find_element(By.ID, "email")
        email.send_keys(email_addr)
        password = self.driver.find_element(By.ID, "PIN")
        password.send_keys(pin)
        button = self.driver.find_element(By.ID, "submit")
        button.click()

    def create_community(self):
        c = Community(communityName="Test Community", category="Sport", description="This is a test community")
        db.session.add(c)
        db.session.commit()

    def create_post(self):
        self.create_community()
        community_first= db.session.query(Community).first()
        author_first= db.session.query(User).first()
        p = Post(topic="Test Post", body="This is a test post", community=community_first, author=author_first)
        db.session.add(p)
        db.session.commit()

    # def test_register_button(self):
    #     # Find the button using its text or other attribute
    #     button = self.driver.find_element(By.XPATH, "//button[text()='Get account']")
    #     button.click()
        
    #     # Allow some time for the navigation
    #     time.sleep(2)

    #     # Verify the URL
    #     current_url = self.driver.current_url
    #     expected_url = localHost + "register"
    #     self.assertEqual(current_url, expected_url)

    # def test_login_button(self):
        
    #     self.actual_login()
    #     current_url = self.driver.current_url
    #     expected_url = localHost + "index"
    #     self.assertEqual(current_url, expected_url)

    # def test_explore_button(self):
    #     self.actual_login()
    #     button = self.driver.find_element(By.XPATH, "//a[text()='Explore']")
    #     button.click()
    #     time.sleep(2)
    #     current_url = self.driver.current_url
    #     if db.session.query(Post).count() == 0:
    #         expected_url = localHost + "community"
    #         self.assertEqual(current_url, expected_url)
    #     else:
    #         expected_url = localHost + "explore"
    #         self.assertEqual(current_url, expected_url)
    
    # def test_explore_button_2(self):
    #     self.actual_login()
    #     self.create_post()
    #     time.sleep(3)
    #     button = self.driver.find_element(By.XPATH, "//a[text()='Explore']")
    #     button.click()
    #     time.sleep(2)
    #     current_url = self.driver.current_url
    #     expected_url = localHost + "explore"
    #     self.assertEqual(current_url, expected_url)

    def test_community_button(self):
        self.actual_login()
        button = self.driver.find_element(By.XPATH, "//a[text()='Community']")
        button.click()
        button_new = self.driver.find_element(By.XPATH, "//button[text()=' NEW FORUM']")
        button_new.click()
        input_commnuity_name = self.driver.find_element(By.ID, "communityName")
        input_commnuity_name.send_keys("Test Community")
        input_description = self.driver.find_element(By.ID, "description")
        input_description.send_keys("This is a test community")
        submit = self.driver.find_element(By.ID, "submit")
        submit.click()
        time.sleep(2)
        messages = self.driver.find_elements(By.CLASS_NAME, "message")
        self.assertEqual(current_url, expected_url)
        

    