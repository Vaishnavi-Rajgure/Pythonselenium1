
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_selected

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("file:///C:/Users/Lenovo/Downloads/MultipleWindow%20(1).html")
sleep(2)
parent=driver.current_window_handle
olive_url="https://www.olivegarden.com/home"
driver.find_element(By.XPATH,"//input[@value='Open Food Sites']").click()
sleep(2)
handles=driver.window_handles
print(handles)
for handle in handles:
    driver.switch_to.window(handle)
    if olive_url==driver.current_url:
        driver.maximize_window()
        driver.back()
        sleep(2)
    else:
        driver.close()
