from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
options.add_argument("--disable-notifications")
expected_url="https://demoapps.qspiders.com/"
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/")
actual_url=driver.current_url
child=driver.window_handles
if actual_url==expected_url:
    print("i am in demo apps page")
    sleep(2)
    driver.find_element(By.XPATH,"// p[contains(text(),'UI Testing Concepts')]").click()
    sleep(2)
    driver.find_element(By.XPATH,"//section[contains(text(),'Popups')]").click()
    sleep(2)
    driver.find_element(By.XPATH,"//section[text()='Javascript']").click()
    sleep(2)
    driver.find_element(By.XPATH,"//button[text()='Alert Box']").click()
    alert=driver.switch_to.alert
    print(alert.text)
    alert.accept()
    sleep(2)
    driver.find_element(By.XPATH, "//section[text()='Browser Windows']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[text()='Open in new window']").click()
    sleep(4)
    driver.switch_to.window(child[0])
    driver.find_element(By.XPATH, "//a[text()='New Tab']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Open window in new Tab']").click()
    sleep(2)
    # driver.back()
    driver.switch_to.window(child[0])
    driver.find_element(By.LINK_TEXT, "Multiple Windows").click()
    sleep(2)
    driver.switch_to.window(child[0])
    driver.find_element(By.LINK_TEXT, "Multiple Tabs").click()
    sleep(2)
else:
    print("i am not in demo apps page ")
driver.back()

driver.find_element(By.XPATH,"//section[contains(text(),'Authentication')]").click()
sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
driver.back()
driver.find_element(By.XPATH,"//section[contains(text(),'Notifications')]")
