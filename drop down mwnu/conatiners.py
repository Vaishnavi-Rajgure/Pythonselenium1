
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("file:///C:/Users/Lenovo/Downloads/demo.html")
sleep(2)
single_Select=driver.find_element(By.ID,"standard_cars")
sel=Select(single_Select)
i=0
for
