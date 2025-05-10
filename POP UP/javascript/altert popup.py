##simple Alert
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=options)
# driver.maximize_window()
# sleep(2)
# driver.get("https://demowebshop.tricentis.com/")
# driver.find_element(By.CSS_SELECTOR,".button-1.search-box-button").click()
# sleep(2)
# alt=driver.switch_to.alert
# print(alt.text)
# alt.accept()



##confirmation Alert
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("https://demo.automationtesting.in/Alerts.html")
sleep(2)
driver.find_element(By.CSS_SELECTOR,".btn.btn-danger").click()
