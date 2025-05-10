import pytest

# @pytest.fixture()
# def setup():
#     print("precondition")
#
# def test_start1(setup):
#     pr
#     int("start1")
# def test_start2(setup):
#     print("start2")


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

from Locators.Tagname import driver


@pytest.mark.parametrize("username,password",[("admin","admin123")])
def test_demo(username,password):
    print(username)
    print(password)
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    sleep(2)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(2)
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys(username)
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password)
    login=driver.find_element(By.XPATH,"//button[@type='submit']")
    login.click()
    # search=driver.find_element(By.XPATH,"//input[@placeholder='Search']")
    # search.send_keys()










