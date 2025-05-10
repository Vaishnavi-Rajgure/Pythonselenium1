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
barbeque_url="https://www.barbequenation.com/"
olive_url="https://www.olivegarden.com/home"
giallozafferano_url="https://www.giallozafferano.com/"
driver.find_element(By.XPATH,"//input[@value='Open Food Sites']").click()
childs=driver.window_handles
for child in childs:
    driver.switch_to.window(child)
    if child!=childs[0]:
        driver.maximize_window()
        sleep(1)
        actual_url=driver.current_url
        if actual_url==barbeque_url:
            driver.find_element(By.XPATH,"//button[@id='hapiness-cart-btn']/following-sibling::button").click()
            sleep(1)

        elif actual_url==olive_url:
            driver.find_element(By.XPATH,"//div[@id='onetrust-close-btn-container']/button").click()

            sleep(2)
            driver.find_element(By.XPATH,"//a[text()='Log In']").click()
            sleep(2)

        elif actual_url==giallozafferano_url:
            sleep(1)
            driver.find_element(By.XPATH,"//div[@class='amecp_cookieBottom']/button").click()
            sleep(1)
            driver.find_element(By.XPATH,"//header[@id='gz-header']/div/span").click()
            sleep(2)
for child in childs:
    driver.switch_to.window(child)
    driver.close()
    sleep(1)
