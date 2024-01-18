from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import ElementClickInterceptedException
import time


TARGET_ACCOUNT = "python.hub"
USERNAME = "pythonpractice_1234"
PASSWORD = "QWERTY12345"

class InstaFollower():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = driver = webdriver.Chrome(options=chrome_options)
    
    def login(self, username, password):
        self.driver.get("https://www.instagram.com/")
        self.username_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.username_field.send_keys(username)

        self.password_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.password_field.send_keys(password)

        self.login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        self.login_button.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get('https://www.instagram.com/python.hub/followers')
        time.sleep(5)
        pop_up_window = WebDriverWait( self.driver, 2).until(EC.element_to_be_clickable( 
        (By.XPATH, "//div[@class='isgrP']")))
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window) 
        
  
    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required.
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


instaBot = InstaFollower()
instaBot.login(USERNAME, PASSWORD)
instaBot.find_followers()
instaBot.follow()