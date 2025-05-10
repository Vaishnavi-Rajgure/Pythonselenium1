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
act.drag_and_drop(source,target).perform()
sleep(2)

source=driver.find_element(By.ID,"box7")
target=driver.find_element(By.ID,"box107")
act.drag_and_drop(source,target).perform()
sleep(2)

source=driver.find_element(By.ID,"box1")
target=driver.find_element(By.ID,"box101")
act.drag_and_drop(source,target).perform()
sleep(2)

source=driver.find_element(By.ID,"box4")
target=driver.find_element(By.ID,"box104")
act.drag_and_drop(source,target).perform()
sleep(2)

source=driver.find_element(By.ID,"box5")
target=driver.find_element(By.ID,"box105")
act.drag_and_drop(source,target).perform()
sleep(2)

source=driver.find_element(By.ID,"box2")
target=driver.find_element(By.ID,"box102")
act.drag_and_drop(source,target).perform()
sleep(2)

source=driver.find_element(By.ID,"box3")
target=driver.find_element(By.ID,"box103")
# act.drag_and_drop(source,target).perform()


#click and Hold
# act.click_and_hold(source).release(target).perform()
sleep(2)

driver.close()