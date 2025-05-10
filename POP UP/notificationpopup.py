from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_selected
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
# driver.get("https://www.easemytrip.com/")
driver.get("https://www.agoda.com/en-in/?cid=1844104&ds=ZTyiRHICzf1nxC73")
sleep(2)

driver.close()