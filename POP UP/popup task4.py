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
nation_url="https://www.barbequenation.com/"
olive_url="https://www.olivegarden.com/home"
giallozafferano_url="https://www.giallozafferano.com/"

driver.find_element(By.XPATH,"//input[@value='Open Food Sites']").click()
sleep(2)
childs=driver.window_handles
for child in childs:
    driver.switch_to.window(child)
    sleep(2)
    if child!=childs[0]:
        print(f"child page url={driver.current_url}")
        sleep(2)
        driver.close()