from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
date=datetime.now()
s=str(date).replace(":","-")
driver.save_screenshot(r"C:\Users\Lenovo\OneDrive\Desktop\screenshot\dws"+s+".png")
sleep(2)
driver.quit()