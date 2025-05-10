from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("https://demoapps.qspiders.com/")
sleep(2)
driver.find_element(By.XPATH,"// p[contains(text(),'UI Testing Concepts')]").click()
sleep(2)
driver.find_element(By.XPATH,"//input[@name='name']").send_keys("krishna")
sleep(2)
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("vaishnavi5@gmail.com")
sleep(2)
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Vaishnavi")
sleep(2)
register= driver.find_element(By.ID,"submit").click()


driver.close()


