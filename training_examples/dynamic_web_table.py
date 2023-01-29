import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://hrm-online.portnov.com/symfony/web/index.php/admin/viewSystemUsers")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID, "txtUsername").send_keys("admin")
driver.find_element(By.ID, "txtPassword").send_keys("password")
driver.find_element(By.ID, "btnLogin").click()

driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']").click()
driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']").click()
driver.find_element(By.ID, "menu_admin_viewSystemUsers").click()

data = driver.find_elements(By.XPATH, "//table[@id='resultTable']/tbody/tr/td")
print("number of all data: ", len(data))


n_rows = len(driver.find_elements(By.XPATH, "//table[@id='resultTable']/tbody/tr"))
print("number of rows: ", n_rows)
user_name = []
user_role = []
for r in range(2, len(data)+1):
    user_name.append(driver.find_element(By.XPATH, "//table[@id='resultTable']/tbody/tr['+str(r)+']/td[2]").text)
    user_role.append(driver.find_element(By.XPATH, "//table[@id='resultTable']/tbody/tr['+str(r)+']/td[3]").text)
print("user name : ", user_name)
print("user role : ", user_role)


driver.close()
