import time
from selenium import webdriver
from selenium.webdriver.common.by import By
opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver=webdriver.Chrome(options=opt)
driver.maximize_window()
time.sleep(1)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(1)
driver.find_element(By.XPATH,"//a[contains(text(),'Digital downloads')]")
time.sleep(1)
album=driver.find_element(By.XPATH,"//a[text()='3rd Album']/../following-sibling::div[3]/div/span")
print(album.text)

music=driver.find_element(By.XPATH,"//a[text()='Music 2']/../../div[3]/div/span")
print(music.text)

Music=driver.find_element(By.XPATH,"//a[text()='Music 2'][2]/../../div[3]/div/span")
print(Music.text)