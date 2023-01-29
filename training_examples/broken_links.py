import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.implicitly_wait(10)
driver.maximize_window()
print(driver.title)

links = driver.find_elements(By.XPATH, '//a')
count = 0
for link in links:
    url = link.get_attribute("href")
    try:
        respond = requests.head(url)
    except:
        None

    if respond.status_code >= 400:
        print(url, "this is a broken link")
        count += 1
    else:
        print(url, "this is valid url")
print('broken links :', count)



driver.close()
