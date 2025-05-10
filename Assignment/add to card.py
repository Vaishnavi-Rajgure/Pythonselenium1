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
driver.get("https://demowebshop.tricentis.com/digital-downloads")
sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Gift Cards')]").click()
sleep(2)
elements=driver.find_elements(By.XPATH,"//div[@class='product-grid']/div/div/div[2]/div[3]/div[2]/input")
for element in elements:
    element.click()
    sleep(1)
    count=driver.find_elements(By.XPATH,"//div[@class='giftcard']/div/input")
    print(count)
    if len(count)==4:
        sleep(1)
    driver.find_elements(By.CLASS_NAME, "recipient-name").send_keys("kanha")
    sleep(1)
    driver.find_elements(By.CLASS_NAME,"recipient-email").send_keys("kanha5@gmail.com")
    sleep(1)
    driver.find_elements(By.CLASS_NAME, "sender-name").send_keys("vaishu")
    sleep(1)
    driver.find_elements(By.CLASS_NAME, "sender-email").send_keys("vaishnavi@gmail.com")
    sleep(1)
    driver.find_elements(By.CLASS_NAME,"message").send_keys("i like this Gift")
else:
    driver.find_elements(By.CLASS_NAME, "recipient-name").send_keys("kanha")
    sleep(1)
    driver.find_elements(By.CLASS_NAME,"sender-name").send_keys("vaishu")
    sleep(1)
    driver.find_elements(By.CLASS_NAME, "message").send_keys("i like this Gift")
    sleep(1)


driver.close()
