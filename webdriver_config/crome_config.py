from selenium import webdriver
import time

class Crome():
    def crome(self):
        driver = webdriver.Chrome(executable_path="E:\\Drivers\\chromedriver.exe")
        driver.get("http://www.google.com/")
        time.sleep(100)

avc = Crome()
avc.crome()
