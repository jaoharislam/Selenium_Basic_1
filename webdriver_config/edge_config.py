from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class orange():
    def Orangee(self):
        driver=webdriver.Chrome(executable_path="E:\\Drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        sarch_bar=driver.find_element(By.NAME,'username')
        passw=driver.find_element(By.NAME,'password')
        login=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        sarch_bar.send_keys('Admin')
        passw.send_keys('Admin123')
        login.click()

        time.sleep(15)




obj=orange()
obj.Orangee()

