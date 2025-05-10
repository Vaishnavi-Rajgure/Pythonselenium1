# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# opt=webdriver.ChromeOptions()
# opt.add_experimental_option("detach",True)
# expected_url="https://demowebshop.tricentis.com/"
# driver=webdriver.Chrome(options=opt)
# driver.maximize_window()
# time.sleep(2)
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# actual_url=driver.current_url
# if expected_url==current_url:
#     print("i am in dws page")
#     searchField=driver.find_element(By.TAG_NAME,"a")
#     searchField.send_keys("vaishnavi")
# else:
#     print("i an not in des page")



# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# opt=webdriver.ChromeOptions()
# opt.add_experimental_option("detach",True)
# expected_url="https://demowebshop.tricentis.com/"
# driver=webdriver.Chrome(options=opt)
# driver.maximize_window()
# time.sleep(2)
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# actual_url=driver.current_url
# if expected_url==actual_url:
#     print("i am in dws page")
#     searchField=driver.find_element(By.TAG_NAME,"a")
#     searchField.send_keys("vaishnavi")
#     time.sleep(2)
#     driver.find_element(By.CLASS_NAME, "ico-register").click()
# else:
#     print("i an not in des page")

#Assignment

# import time
# from multiprocessing.resource_tracker import register
# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# opt=webdriver.ChromeOptions()
# opt.add_experimental_option("detach",True)
# expected_url="https://demowebshop.tricentis.com/"
# driver=webdriver.Chrome(options=opt)
# driver.maximize_window()
# time.sleep(2)
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# actual_url=driver.current_url
# if expected_url==actual_url:
#     print("i am in dws page")
#     searchField=driver.find_element(By.TAG_NAME,"input")
#     searchField.send_keys("vaishnavi")
#     time.sleep(1)
#     register=driver.find_element(By.CLASS_NAME, "ico-register").click()
#     send=driver.find_element(By.ID,"small-searchterms").send_keys("laptop")
#
#     name=driver.find_element(By.NAME,"FirstName").send_keys("vaishu")
#     time.sleep(1)
#     gender=driver.find_element(By.ID,"gender-female").click()
#     time.sleep(1)
#     lastname = driver.find_element(By.ID,"LastName").send_keys("Rajgure")
#     time.sleep(1)
#     Email =driver.find_element(By.ID,"Email").send_keys("vaishu@5gmail.com")
#     time.sleep(1)
#     psd= driver.find_element(By.ID,"Password").send_keys("vaishu@123")
#     time.sleep(1)
#     psd1= driver.find_element(By.ID,"ConfirmPassword").send_keys("vaishu@123")
#     register1= driver.find_element(By.ID,"register-button").click()
# else:
#     print("i an not in des page")
#


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver=webdriver.Chrome(options=opt)
driver.maximize_window()
time.sleep(2)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)
driver.find_element(By,X)



