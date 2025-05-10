from time import sleep
from unittest.mock import right

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
act=ActionChains(driver)
right=driver.find_element(By.XPATH,"//span[text()='right click me']")
act.context_click(right).perform()
sleep(2)
demo1=driver.find_element(By.XPATH,"//span[text()='Edit']")
new1=ActionChains(driver)
new1.context_click(demo1).perform()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
sleep(2)

right=driver.find_element(By.XPATH,"//span[text()='right click me']")
act.context_click(right).perform()
demo2=driver.find_element(By.XPATH,"//span[text()='Cut']")
new2=ActionChains(driver)
new2.context_click(demo2).perform()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
sleep(2)

right=driver.find_element(By.XPATH,"//span[text()='right click me']")
act.context_click(right).perform()
demo=driver.find_element(By.XPATH,"//span[text()='Copy']")
new=ActionChains(driver)
new.context_click(demo).perform()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
sleep(2)

right=driver.find_element(By.XPATH,"//span[text()='right click me']")
act.context_click(right).perform()
demo3=driver.find_element(By.XPATH,"//span[text()='Paste']")
new3=ActionChains(driver)
new3.context_click(demo3).perform()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
sleep(2)

right=driver.find_element(By.XPATH,"//span[text()='right click me']")
act.context_click(right).perform()
demo3=driver.find_element(By.XPATH,"//span[text()='Delete']")
new3=ActionChains(driver)
new3.context_click(demo3).perform()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
sleep(2)

right=driver.find_element(By.XPATH,"//span[text()='right click me']")
act.context_click(right).perform()
demo3=driver.find_element(By.XPATH,"//span[text()='Quit']")
new3=ActionChains(driver)
new3.context_click(demo3).perform()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
driver.close()
