from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("file:///C:/Users/Lenovo/Downloads/demo.html")
sleep(2)
multi_select=driver.find_element(By.ID,"multiple_cars")
sel=Select(multi_select)

sel.select_by_visible_text("BMW")
sleep(2)
sel.select_by_value("aud")
sleep(2)
sel.select_by_index(5)

#it is used deselect method
sleep(2)
sel.deselect_by_visible_text("BMW")
sleep(2)
sel.deselect_by_value("aud")
sleep(2)
sel.deselect_by_index(5)
sleep(2)
sel.deselect_all()
driver.close()