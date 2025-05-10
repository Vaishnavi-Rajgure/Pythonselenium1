from selenium import webdriver
from time import sleep
def test_dws():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://demowebshop.tricentis.com/")
    driver.close()
def test_rcb():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.royalchallengers.com/")
    print("ye sala cup hame de")
    driver.close()
def test_csk():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.cricbuzz.com/cricket-team/chennai-super-kings/58")
    print("thala for a reason")
    driver.close()
def test_mi():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.mumbaiindians.com/")
    print("Hit man of india")
    driver.close()