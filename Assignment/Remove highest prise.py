import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_title=""
driver=webdriver.Chrome(options=options)
driver.maximize_window()
time.sleep(2)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)
driver.find_element(By.XPATH,"").click()
time.sleep(2)