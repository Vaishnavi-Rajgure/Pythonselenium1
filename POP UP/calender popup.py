
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.easemytrip.com/")
sleep(2)
driver.find_element(By.ID,"dvfarecal").click()
sleep(2)
driver.find_element(By.ID,"fst_5_04/04/2025").click()
sleep(2)
driver.find_element(By.ID,"divRtnCal").click()
sleep(2)
driver.find_element(By.ID,"img2Nex").click()
sleep(2)
driver.find_element(By.ID,"img2Nex").click()
sleep(2)
driver.find_element(By.ID,"img2Nex").click()
sleep(2)
driver.find_element(By.ID,"frth_3_23/07/2025").click()
# while True:
#     try:
#         driver.find_element(By.ID, "frth_3_23/07/2025").click()
#         break
#     except:
#         driver.find_element(By.ID, "img2Nex").click()
# sleep(2)
driver.close()

