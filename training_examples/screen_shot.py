import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

ops = webdriver.EdgeOptions()
ops.headless = False
ops = webdriver.EdgeOptions()
ops.headless = False

driver = webdriver.Edge(options=ops)


driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
print ( driver.title )
# driver.save_screenshot(os.getcwd()+"//home_page.png")
driver.save_screenshot("C:/Usersrusgl/PycharmProjects/Training/training_examples/home_page1.png")

cookies = driver.get_cookies()
print ( "cookies: ", len(cookies ) )



driver.close()
