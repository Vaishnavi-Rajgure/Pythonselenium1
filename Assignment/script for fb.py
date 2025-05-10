from time import sleep

from select import select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_title=""
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("https://www.facebook.com/")
sleep(2)
driver.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()
sleep(2)
driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Vaishu")
sleep(2)
driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys("rajguru")
single_select=driver.find_element(By.ID,"day")
sel=Select(single_select)
sel.select_by_visible_text("4")
sleep(2)
single_select=driver.find_element(By.ID,"month")
sel1=Select(single_select)
sel1.select_by_visible_text("Apr")
sleep(2)
single_select=driver.find_element(By.ID,"year")
sel2=Select(single_select)
sel2.select_by_visible_text("2002")
sleep(2)
driver.find_elements(By.XPATH,"//input[@name='sex']").click()
sleep(2)




driver.close()





