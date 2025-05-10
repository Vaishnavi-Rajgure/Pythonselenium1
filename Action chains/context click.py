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
right=driver.find_element(By.XPATH,"//span[text()='right click me']")
act=ActionChains(driver)
act.context_click(right).perform()
sleep(2)
demo=driver.find_element(By.XPATH,"//span[text()='Copy']")
new=ActionChains(driver)
new.context_click(demo).perform()
