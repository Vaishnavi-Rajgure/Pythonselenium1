
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=options)
# driver.maximize_window()
# sleep(2)
# driver.get("https://demowebshop.tricentis.com/")
# sleep(2)
# driver.find_element(By.XPATH,"//a[contains(text(),'Digital downloads')]").click()
# sleep(1)
# sort_by=driver.find_element(By.ID,"products-orderby")
# sel=Select(sort_by)
# ranges=sel.options
# i=0
# for range in ranges:
#     sort_by = driver.find_element(By.ID, "products-orderby")
#     sel = Select(sort_by)
#     sel.select_by_index(i)
#     i+=1
#     sleep(2)
# driver.close()


# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=options)
# driver.maximize_window()
# sleep(2)
# driver.get("https://demowebshop.tricentis.com/")
# driver.find_element(By.XPATH,"//a[contains(text(),'Digital downloads')]").click()
# sleep(1)
# sort_by=driver.find_element(By.ID,"products-pagesize")
# sel=Select(sort_by)
# ranges=sel.options
# i=0
# for range in ranges:
#     sort_by = driver.find_element(By.ID,"products-pagesize")
#     sel=Select(sort_by)
#     sel.select_by_index(i)
#     i+=1
#     sleep(2)
# driver.close()
#


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("https://demowebshop.tricentis.com/")
driver.find_element(By.XPATH,"//a[contains(text(),'Digital downloads')]").click()
sleep(1)
sort_by=driver.find_element(By.ID,"products-viewmode")
sel=Select(sort_by)
ranges=sel.options
i=0
for range in ranges:
    sel.select_by_index(i)
    i+=1
    sleep(2)
driver.close()