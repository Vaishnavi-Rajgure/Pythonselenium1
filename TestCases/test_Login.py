import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup1")
class test_Login:
    def test_tc_01(self):
        expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)
        assert self.driver.current_url==expected_url, "login not successfull"
        print("login not successfull")
        time.sleep(4)

    def test_tc_02(self):
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("adm213")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        assert self.driver.current_url == expected_url, "login successfull  defect is found"
        print("login successfull")
        time.sleep(5)

    def test_tc_03(self):
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys(" ")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        assert self.driver.current_url == expected_url, "login not successfull"
        print("login not successfull")
        time.sleep(4)

    def test_tc_04(self):
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//p[text()='Forgot your password? ']").click()
        time.sleep(2)
        assert self.driver.current_url == expected_url, "Reset password"
        print("login not successfull")
        time.sleep(4)
