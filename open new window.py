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
parent=driver.current_window_handle
print(parent)
print(type(parent))
driver.find_element(By.XPATH,"// p[contains(text(),'UI Testing Concepts')]").click()
sleep(2)
driver.find_element(By.XPATH,"//section[contains(text(),'Popups')]").click()
sleep(2)
driver.find_element(By.XPATH,"//section[contains(text(),'Browser Windows')]").click()
sleep(2)

child=driver.window_handles
driver.switch_to.window(child[1])

driver.find_element(By.XPATH,"//a[contains(text(),'New Window')]").click()

driver.find_element(By.XPATH,"//button[text()='Open window in new Tab']").click()