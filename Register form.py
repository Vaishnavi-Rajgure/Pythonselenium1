

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("https://demo.automationtesting.in/Register.html")
sleep(2)
driver.find_element(By.XPATH,"//input[@ng-model='FirstName']").send_keys("vaishnavi")
sleep(1)
driver.find_element(By.XPATH,"//input[@ng-model='LastName']").send_keys("Rajgure")
sleep(1)
driver.find_element(By.XPATH,"//textarea[@ng-model='Adress']").send_keys("Ghatanji")
sleep(1)
driver.find_element(By.XPATH,"//input[@ng-model='EmailAdress']").send_keys("vaishnavi5@gmail.com")
sleep(1)

action=ActionChains(driver)
action.key_down(Keys.TAB).perform()
action.send_keys("8378097787").perform()
action.key_down(Keys.ENTER).perform()

driver.find_element(By.XPATH,"//input[@value='FeMale']").click()
sleep(1)
driver.find_element(By.XPATH,"//input[@id='checkbox2']").click()
driver.find_element(By.XPATH,"//input[@id='checkbox3']").click()

# lang=driver.find_element(By.XPATH,"//div[@id='msdd']").click()
# sleep(1)
# driver.find_element(By.XPATH,"//a[text()='English']").click()
# driver.find_element(By.XPATH,"//a[text()='English']").click()

action.key_down(Keys.PAGE_DOWN).perform()

single_select=driver.find_element(By.ID,"Skills")
sel=Select(single_select)
sel.select_by_visible_text("HTML")

single_select=driver.find_element(By.ID,"select2-country-container")
sel=Select(single_select)
sel.select_by_value(4)

single_select=driver.find_element(By.ID,"yearbox")
sel=Select(single_select)
sel.select_by_visible_text("2002")
sleep(2)
single_select=driver.find_element(By.ID,"monthbox")
sel1=Select(single_select)
sel1.select_by_visible_text("April")
sleep(2)
single_select=driver.find_element(By.ID,"daybox")
sel2=Select(single_select)
sel2.select_by_visible_text("4")
sleep(2)

driver.find_element(By.XPATH,"//input[@ng-model='Password']").send_keys("vaishu@123")
driver.find_element(By.XPATH,"//input[@ng-model='CPassword']").send_keys("vaishu@123")
sleep(1)

driver.find_element()