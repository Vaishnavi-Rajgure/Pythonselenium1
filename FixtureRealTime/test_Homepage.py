import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("setup")
class TestCase1:
   def test_admin(self):
       time.sleep(3)
       self.driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active']").send_keys("admin")
       time.sleep(3)
       admin=self.driver.find_element(By.XPATH,"//span[text()='Admin']")
       time.sleep(3)
       assert admin.is_displayed(),"admin is not present"
       print("admin is present")

   def test_pim(self):
       time.sleep(2)
       pim = self.driver.find_element(By.XPATH, "//span[text()='PIM']")
       time.sleep(2)
       assert pim.is_displayed(), "pim is not present"
       print("pim is present")

