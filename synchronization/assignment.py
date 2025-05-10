from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
wait=WebDriverWait(driver,30)
driver.get("https://omayo.blogspot.com/")
driver.find_element(By.XPATH,"//button[text()='Dropdown']").click()
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Facebook')]")))
driver.find_element(By.XPATH,"//a[contains(text(),'Facebook')]").click()
driver.back()
wait.until(expected_conditions.element_to_be_clickable((By.ID,"timerButton")))
driver.find_element(By.ID,"timerButton").click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
