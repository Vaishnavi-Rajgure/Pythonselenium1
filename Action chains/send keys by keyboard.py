from re import search

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
# action.key_down(Keys.TAB).perform()
# action.key_down(Keys.TAB).perform()
# action.key_down(Keys.TAB).perform()
# action.key_down(Keys.TAB).perform()
# action.key_down(Keys.TAB).perform()
# action.key_down(Keys.TAB).perform()
# sleep(2)
# action.send_keys("Laptop").perform()
# sleep(2)
# action.key_down(Keys.ENTER).perform()
search=driver.find_element(By.ID,"small-searchterms")
action.send_keys_to_element(search,"laptop").perform()