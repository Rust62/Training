import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
act = ActionChains(driver)
act.context_click(button).perform()   # Right click!

# act.double_click(button).perform()    #Double click!
# act.release()
# act.click_and_hold()
# act.drag_and_drop()


time.sleep(3)

driver.close()



