import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//*[@id='dob']").click()
year = "2020"
month = "May"
day = "25"


years = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectYear']"))
years.select_by_visible_text(year)

months = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']"))
months.select_by_visible_text(month)


days = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for ele in days:
    if ele.text == day:
        ele.click()
        break

time.sleep(3)
driver.close()
