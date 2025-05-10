from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("https://demowebshop.tricentis.com/digital-downloads")
sleep(2)
act=ActionChains(driver)
# act.key_down(Keys.PAGE_DOWN).perform()
sleep(2)
# act.key_down(Keys.PAGE_DOWN).perform()
facebook=driver.find_element(By.XPATH,"//a[text()='Facebook']")
act.scroll_to_element(facebook).perform()
sleep(4)

driver.close()