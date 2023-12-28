from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

TARGET_ACCOUNT = "python.hub"
USERNAME = "pythonpractice_1234"
PASSWORD = "QWERTY12345"

driver.get("https://www.instagram.com/")

username_field = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
username_field.send_keys(USERNAME)

password_field = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password_field.send_keys(PASSWORD)

login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
login_button.click()

