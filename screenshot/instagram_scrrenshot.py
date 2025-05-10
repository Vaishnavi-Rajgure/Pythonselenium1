from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/shahidkapoor/?hl=en")
sleep(2)
logo=driver.find_element(By.XPATH,"//img[@crossorigin='anonymous']")
logo.screenshot("insta_dp.png")
sleep(2)
driver.quit()