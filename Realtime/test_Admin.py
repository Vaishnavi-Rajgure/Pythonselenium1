import time

from selenium import webdriver
from selenium.webdriver import ActionChains ,Keys
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
    driver.find_element(By.XPATH,"//ul[@class='oxd-main-menu']/li[1]").click()
    driver.find_element(By.XPATH,"//div[@class='orangehrm-header-container']/button").click()
    driver.find_element(By.XPATH,"//div[@class='oxd-select-text-input']").click()
    time.sleep(2)
    act=ActionChains(driver)
    act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[2]").click()
    time.sleep(2)
    act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    driver.find_element(By.XPATH,"//input[@type='password']").send_keys("vaishu123")
    driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("Ali Hamed")
    time.sleep(2)
    act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active']").send_keys("helloo")
    driver.find_element(By.XPATH,"//input[@type='password']").send_keys("vaishu123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
