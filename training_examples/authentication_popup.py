import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome()

# how to get round authentication-popup

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()

time.sleep(3)
driver.close()
