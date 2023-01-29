import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.nopcommerce.com/en/demo")
driver.implicitly_wait(10)
driver.maximize_window()
print(driver.title)

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
i = 0
for link in links:
    i += 1
    print('This is a link text: ', i, link.text)





driver.close()





