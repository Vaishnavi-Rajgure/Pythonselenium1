import time

from selenium import webdriver
# from selenium.webdriver import ActionChains ,Keys
from selenium.webdriver.common.by import By


def test_dws():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.NAME,"password").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//li[@class='oxd-main-menu-item-wrapper'][2]//span").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='orangehrm-header-container']//button").click()
    time.sleep(4)
    driver.find_element(By.NAME,"firstName").send_keys("vaishnav")
    driver.find_element(By.NAME,"middleName").send_keys("D")
    driver.find_element(By.NAME, "lastName").send_keys("Raj")
    time.sleep(4)
    driver.find_element(By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
    time.sleep(4)

    driver.find_element(By.XPATH,"")

    driver.find_element(By.XPATH,"//input[@type='password']").send_keys("vaish2002")
    driver.find_element(By.XPATH,"")
    time.sleep(4)













    # driver.find_element(By.XPATH,"//button[@type='submit']").click()
    # time.sleep(4)
    # driver.find_element(By.XPATH,"//li[@class='oxd-main-menu-item-wrapper'][2]//span").click()
    # time.sleep(4)
    # driver.find_element(By.XPATH,"//label[contains(text(),'Employee Id')]").send_keys("4051")