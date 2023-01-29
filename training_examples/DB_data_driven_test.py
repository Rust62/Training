import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import mysql.connector

driver = webdriver.Chrome ()
driver.get (
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html"
)
driver.implicitly_wait ( 10 )
driver.maximize_window ()

# try:
con = mysql.connector.connect ( host="127.0.0.1" , port=3306 , user='root' , passwd='1999' , database='sql_mydb' )
curs = con.cursor ()
curs.execute ( "select * from test_data" )
Actual_Maturity_value = driver.find_element ( By.XPATH , "//*[@id='resp_matval']/strong" ).text
print(Actual_Maturity_value)
for row in curs:

    Principal = row[0]
    Rate_of_interest = row[1]
    Period1 = row[2]
    Period2 = row[3]
    Frequency = row[4]
    Maturity_value = row[5]

    driver.find_element ( By.XPATH , "//input[@id='principal']" ).send_keys ( Principal )
    driver.find_element ( By.XPATH , "//*[@id='interest']" ).send_keys ( Rate_of_interest )
    driver.find_element ( By.XPATH , "//*[@id='tenure']" ).send_keys ( Period1 )
    Per2 = Select ( driver.find_element ( By.XPATH , "//select[@id='tenurePeriod']" ) )
    Per2.select_by_visible_text ( Period2 )

    FR = Select ( driver.find_element ( By.XPATH , "//select[@id='frequency']" ) )
    FR.select_by_visible_text ( Frequency )

    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()

    Actual_Maturity_value = driver.find_element ( By.XPATH , "//*[@id='resp_matval']/strong" ).text
    print(Actual_Maturity_value)

    print ( driver.find_element ( By.XPATH , " //*[@id='fdMatVal']/div[2]/a[2]/img" ).click () )

    # if  Maturity_value == Actual_Maturity_value:
    #     print ( "Passed" )
    #     print ( Actual_Maturity_value , Maturity_value )
    # else:
    #     print ( "Failed" )
    # time.sleep ( 2 )
    # driver.find_element ( By.XPATH , "/html[1]/body[1]/div[8]/div[2]/div[1]/div[5]/div[1]/div[1]/div[3]/form[1]/div[2]/a[2]/img[1]" ).click()

con.close ()

# except:
#     print ( "connection unsuccessful..." )

driver.close ()
