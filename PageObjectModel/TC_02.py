
import time
from selenium import webdriver

from PageObjectModel.Homepage import Admin
from PageObjectModel.Loginpage import Login
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
expected_url1="https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
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

log2=Admin(driver)
time.sleep(2)
log2.click_admin()
time.sleep(2)
assert expected_url1==driver.current_url,"you are not in user admin page"
print("you are in user admin page")
log2.click_add()
time.sleep(2)

log3=UserAdmin(driver)
time.sleep(2)
log3.click_select()
time.sleep(2)
action = ActionChains(driver)
action.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
time.sleep(2)
log3.click_status()
time.sleep(2)
action.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
time.sleep(2)
log3.send_pass("vaishu123")
time.sleep(2)
log3.send_Emp("Call Sunny")
time.sleep(2)
action.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
log3.send_User("empty")
time.sleep(2)
log3.confpwd("vaishu123")
time.sleep(2)
log3.click_sub()
driver.quit()

