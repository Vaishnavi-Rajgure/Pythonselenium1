from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_selected

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("https://demowebshop.tricentis.com/digital-downloads")
sleep(2)
parent=driver.current_window_handle
print(parent)
print(type(parent))
action=ActionChains(driver)
action.key_down(Keys.PAGE_DOWN).perform()
driver.find_element(By.XPATH,"//a[text()='Facebook']").click()
sleep(2)
child=driver.window_handles
driver.switch_to.window(child[1])
sleep(2)
driver.find_element(By.XPATH,"//span[text()='Create new account']").click()

driver.find_element(By.XPATH,"//a[text()='Twitter']").click()
# sleep(2)
# child1=driver.window_handles
# driver.switch_to.window(child1[2])
# driver.find_element(By.XPATH,"//span[text()='Create account']").click()