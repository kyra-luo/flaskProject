
import multiprocessing
import time
from unittest import TestCase 
from selenium import webdriver  
from app import create_app, db
from config import SeleniumConfig, TestingConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.models import User, Post, Comment, Community
from werkzeug.security import generate_password_hash, check_password_hash
from app.helpers import generate_user_id, generate_random_email, generate_random_string

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


    def actual_login(self):
        p = generate_password_hash('cat')
        email_addr = generate_random_email()
        fname = generate_random_string(5)
        lname = generate_random_string(5)
        username = generate_random_string(5)
        u = User(username=username, User_id=Uid, fname=fname, lname=lname, email=email_addr, password_hash=p)
        db.session.add(u)
        db.session.commit()
        time.sleep(2)
        pin="cat"
        login_url = f"http://localhost:8000/login"
        self.driver.get(login_url)
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

    def test_register_button(self):
        # Find the button using its text or other attribute
        button_next = self.driver.find_element(By.ID, "nextButton")
        button_next.click()
        button_next.click()
        button_enter = self.driver.find_element(By.ID, "navigateWord")
        button_enter.click()
        button = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Get account']"))
        )
        
        button.click()
        time.sleep(2)

        # Verify the URL
        current_url = self.driver.current_url
        expected_url = localHost + "register"
        self.assertEqual(current_url, expected_url)

    def test_login_button(self):
        self.actual_login()
        current_url = self.driver.current_url
        expected_url = localHost + "index"
        self.assertEqual(current_url, expected_url)

    def test_explore_button(self):
        self.actual_login()
        button_next = self.driver.find_element(By.ID, "nextButton")
        button_next.click()
        time.sleep(2)
        button_enter = self.driver.find_element(By.ID, "navigateWord")
        button_enter.click()
        current_url = self.driver.current_url
        if db.session.query(Post).count() == 0:
            expected_url = localHost + "community"
            self.assertEqual(current_url, expected_url)
        else:
            expected_url = localHost + "explore"
            self.assertEqual(current_url, expected_url)
    
    def test_explore_button_2(self):
        self.actual_login()
        self.create_post()
        time.sleep(3)
        button_next = self.driver.find_element(By.ID, "nextButton")
        button_next.click()
        button_enter = self.driver.find_element(By.ID, "navigateWord")
        button_enter.click()
        current_url = self.driver.current_url
        expected_url = localHost + "explore"
        self.assertEqual(current_url, expected_url)

    def test_community_button(self):
        self.actual_login()
        community_url = f"http://localhost:8000/community"
        self.driver.get(community_url)
        button_new = self.driver.find_element(By.XPATH, "//button[@data-bs-toggle='modal' and @data-bs-target='#forumModal']")
        button_new.click()
        input_community_name = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.ID, "communityName"))
        )
        # Scroll into view if needed
        # self.driver.execute_script("arguments[0].scrollIntoView();", input_community_name)
        
        # Send keys to the input field
        input_community_name.send_keys("Test Community")
        input_description = self.driver.find_element(By.ID, "description")
        input_description.send_keys("This is a test community")
        submit = self.driver.find_element(By.ID, "submit")
        submit.click()
        time.sleep(2)
        messages = self.driver.find_elements(By.CLASS_NAME, "alert")
        self.assertEqual(len(messages), 1, "Expected there to be a single error message when trying to create a community")
        

    