import time

import openpyexcel
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from training_examples import XL_Utilitis as xl

driver = webdriver.Chrome()
driver.get(
"https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html"
)
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element ( By.XPATH , "//*[@id='fdMatVal']/div[2]/a[2]/img" ).click ()
file = "C:/Users/rusgl/Desktop/Test_data.xlsx"
workbook = openpyxl.load_workbook(file)
row_num = xl.get_row_count(file, "Sheet1")

for r in range(3, row_num + 1):
    Principal = xl.read_data(file, "Sheet1", r, 1)
    Rate_of_interest = xl.read_data(file, "Sheet1", r, 2)
    Period1 = xl.read_data(file, "Sheet1", r, 3)
    Period2 = xl.read_data(file, "Sheet1", r, 4)
    Frequency = xl.read_data(file, "Sheet1", r, 5)
    Expected = xl.read_data(file, "Sheet1", r, 6)

    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(Principal)
    driver.find_element(By.XPATH, "//*[@id='interest']").send_keys(Rate_of_interest)
    driver.find_element(By.XPATH, "//*[@id='tenure']").send_keys(Period1)
    Per2 = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    Per2.select_by_visible_text(Period2)

    FR = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    FR.select_by_visible_text(Frequency)

    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    Actual_Maturity_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    if float(Actual_Maturity_value) == float(Expected):
        print("Test Passed")
        xl.write_data(file, "Sheet1", r, 8, "Passed")
        xl.fill_green_color(file, "Sheet1", r, 8)
        print(Actual_Maturity_value)
    else:
        print("Test Failed")
        xl.write_data(file, "Sheet1", r, 8, "Failed")
        xl.fill_red_color(file, "Sheet1", r, 8)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()

driver.close()
