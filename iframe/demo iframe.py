from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--disable-notification")
expected_url="https://demoapps.qspiders.com/"
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/")
sleep(2)
actual_url=driver.current_url
child=driver.window_handles
if actual_url==expected_url:
    driver.find_element(By.XPATH, "// p[contains(text(),'UI Testing Concepts')]").click()
    sleep(2)
    driver.find_element(By.XPATH,"//section[text()='Frames']").click()
    sleep(2)
driver.find_element(By.LINK_TEXT,"iframes").click()
sleep(2)
driver.switch_to.frame(0)
driver.find_element(By.ID,"username").send_keys("Vaishnavi")
sleep(2)
driver.find_element(By.ID,"password").send_keys("v@1233")
sleep(1)
driver.find_element(By.ID,"submitButton").click()
