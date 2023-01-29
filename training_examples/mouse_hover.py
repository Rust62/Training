import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://hrm-online.portnov.com/symfony/web/index.php/admin/viewSystemUsers")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID, "txtUsername").send_keys("admin")
driver.find_element(By.ID, "txtPassword").send_keys("password")
driver.find_element(By.ID, "btnLogin").click()

admin = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']")
user_management = driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
user = driver.find_element(By.ID, "menu_admin_viewSystemUsers")

act = ActionChains(driver)
act.move_to_element(admin).move_to_element(user_management).move_to_element(user).click().perform()

time.sleep(3)
driver.close()
