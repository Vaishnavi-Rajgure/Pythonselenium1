from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--disable-notification")
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.shoppersstack.com/")
driver.find_element(By.ID,"loginBtn").click()
driver.find_element(By.XPATH,"//span[text()='Create Account']").click()
