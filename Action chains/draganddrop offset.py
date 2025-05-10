from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
sleep(2)
act=ActionChains(driver)
source=driver.find_element(By.ID,"box6")
target=driver.find_element(By.ID,"box106")
act.drag_and_drop_by_offset(source,"818","306").perform()
sleep(2)