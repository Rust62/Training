import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)
alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys("welcome")
alert_window.accept()
time.sleep(3)
driver.close()
