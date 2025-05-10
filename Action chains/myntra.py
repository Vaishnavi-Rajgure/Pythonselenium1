from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("https://www.myntra.com/?utm_source=dms_google&utm_medium=searchbrand_cpc&utm_campaign=dms_google_searchbrand_cpc_Search_Brand_Myntra_Brand_"
           "India_BM_TROAS_SOK_New&gad_source=1&gclid=EAIaIQobChMImsKT5t75iwMVbso8Ah1pOjrvEAAYASAAEgLZ_PD_BwE")
kid=driver.find_element(By.ID,"//[contains(text(),'Kids')]")
sleep(2)
act=ActionChains(driver)
act.move_to_element(kid).perform()
soft=driver.find_element(By.ID,"//a[contain(text(),'soft toys')]")
act.move_to_element(soft).click("Soft Toys").perform()

