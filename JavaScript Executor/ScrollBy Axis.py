from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
sleep(2)
##ScrollBy
act=ActionChains(driver)
act.key_down(Keys.PAGE_DOWN).perform()
driver.execute_script("window.scrollBy(0,1000);")
# driver.execute_script("window.scrollBy(0,500);")


##ScrollTo
# driver.execute_script("window.scrollTo(0,1000);")
# sleep(2)
# driver.execute_script("window.scrollTo(0,-1000);")

