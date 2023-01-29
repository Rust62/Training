import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome()

driver.get("https://mypage.rediff.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@value=' Go ']").click()
time.sleep(3)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()


time.sleep(3)

driver.close()
