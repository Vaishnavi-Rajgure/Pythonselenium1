from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
action=ActionChains(driver)
action.key_down(Keys.TAB).perform()
action.key_down(Keys.TAB).perform()
action.key_down(Keys.ENTER).perform()
driver.find_element(By.XPATH,"//div[2][@class='gender']").click()
action.key_down(Keys.ENTER).perform()

action.send_keys("VAISHU").perform()
action.key_down(Keys.ENTER).perform()
sleep(2)
action.send_keys("RAJGURE").perform()
action.key_down(Keys.ENTER).perform()
sleep(2)
action.send_keys("vaishnavi5@gmail.com").perform()
action.key_down(Keys.ENTER).perform()
sleep(2)
action.send_keys("vaishu1234").perform()
action.key_down(Keys.ENTER).perform()
sleep(2)
action.send_keys("vaishu1234").perform()

driver.close()

