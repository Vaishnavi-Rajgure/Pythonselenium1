from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
sleep(2)
dropdown=driver.find_element(By.XPATH,"//button[@class='dropbtn']")
# driver.execute_script("arguments[0].scrollIntoView(false);",dropdown)
# when we are providing false webelement is present in bottom

driver.execute_script("arguments[0].scrollIntoView(true);",dropdown)
##when we are providing true webelemnet is present in top
