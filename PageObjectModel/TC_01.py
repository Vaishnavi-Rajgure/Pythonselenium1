import time
from selenium import webdriver
from PageObjectModel.Loginpage import Login

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
driver.implicitly_wait(15)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
log=Login(driver)
log.send_username("Admin")
time.sleep(2)
log.send_password("admin123")
time.sleep(2)
log.click_login_button()
time.sleep(2)
actual_url=driver.current_url
assert expected_url==actual_url,"login is unsuccessfull"
print("login is successfull")
driver.quit()