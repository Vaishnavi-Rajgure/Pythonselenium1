from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.naukri.com/")
sleep(2)
driver.find_element(By.ID,"register_Layer").click()
sleep(2)
driver.find_element(By.XPATH,"//input[@placeholder='What is your name?']").send_keys("vaishnavi Rajgure")
sleep(2)
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("vaishnavirajgure5@gmail.com")
sleep(2)
driver.find_element(By.ID,"password").send_keys("Vaishu@2002")
sleep(2)
driver.find_element(By.ID,"mobile").send_keys("9284436784")
sleep(2)

