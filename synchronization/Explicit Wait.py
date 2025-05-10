from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--disable-notification")
driver=webdriver.Chrome(options=options)
driver.maximize_window()
wait=WebDriverWait(driver,30)
driver.get("https://www.shoppersstack.com/")
wait.until(expected_conditions.visibility_of_element_located((By.ID,"loginBtn")))
driver.find_element(By.ID,"loginBtn").click()
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//span[text()='Create Account']")))
driver.find_element(By.XPATH,"//span[text()='Create Account']").click()
