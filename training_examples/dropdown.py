import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.implicitly_wait(10)
driver.maximize_window()
print(driver.title)

# dpr_country_ele = driver.find_element(By.XPATH, "//select[@id='input-country']")
# dpr_country = Select(dpr_country_ele)
# dpr_country = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))
# dpr_country.select_by_visible_text('Azerbaijan')
# dpr_country.deselect_by_visible_text('Azerbaijan')
# dpr_country.select_by_value('15')
# dpr_country.deselect_by_value('15')

all_options = driver.find_elements(By.XPATH, "//*[@id='input-country']/option")
print ( len ( all_options ) )


time.sleep(3)
driver.close()



