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
driver.find_element(By.ID,"password").send_keys("v@123")
sleep(1)
driver.find_element(By.ID,"submitButton").click()
sleep(2)
driver.switch_to.parent_frame()
driver.find_element(By.LINK_TEXT,"Nested iframe").click()
sleep(2)
driver.switch_to.frame(2)
driver.find_element(By.ID,"email").send_keys("vaishnavi4@gmail.com")
driver.find_element(By.ID,"password").send_keys("V@123")
driver.find_element(By.ID,"confirm-password").send_keys("V@123")

# driver.switch_to.parent_frame()
# driver.find_element(By.LINK_TEXT,"Multiple iframe").click()
# driver.switch_to.frame(1)
# driver.find_element(By.ID,"email").send_keys("vaishnavi4@gmail.com")
# driver.find_element(By.ID,"password").send_keys("V@1233")
# driver.find_element(By.ID,"confirm-password").send_keys("V@1233")