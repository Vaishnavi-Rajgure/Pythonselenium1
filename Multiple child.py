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
parent=driver.current_window_handle
expected_res="https://demowebshop.tricentis.com/news/rss/1"
twitter_url="https://x.com/nopCommerce"
facebook_url="https://www.facebook.com/nopCommerce"
youtube_url="https://www.youtube.com/user/nopCommerce"
google_url="https://workspaceupdates.googleblog.com/2023/04/new-community-features-for-google-chat-and-an-update-currents%20.html"

action=ActionChains(driver)
action.key_down(Keys.PAGE_DOWN).perform()
sleep(2)
links=driver.find_elements(By.XPATH,"//div[@class='column follow-us']/ul/li/a")
for link in links:
    actual_url1=driver.current_url
    if expected_res==actual_url1:
        driver.back()
    link.click()
    sleep(1)
childs=driver.window_handles
sleep(2)
for child in childs:
    driver.switch_to.window(child)
    actual_url2=driver.current_url
    if twitter_url==actual_url2:
        sleep(1)
        print("i am in twitter page")
        driver.find_element(By.XPATH,"//span[text()='Create account']").click()
    elif facebook_url==actual_url2:
        sleep(1)
        print("i am in facebook page")
        driver.find_element(By.XPATH, "//span[text()='Create new account']").click()
    elif youtube_url==actual_url2:
        sleep(1)
        print("i am in youtube page")
        driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("arjit singh songs")
        action.key_down(Keys.ENTER)
    elif google_url==actual_url2:
        sleep(1)
        print("i am in google page")
        driver.find_element(By.XPATH,"//input[@id='mce-EMAIL']").send_keys("vaishnavi")
sleep(1)


