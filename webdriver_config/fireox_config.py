from selenium import webdriver
import time

class runfirefox():
    def firefoxx(self):
        driver =webdriver.Firefox(executable_path="E:\\Drivers\\geckodriver.exe")
        driver.minimize_window()
        time.sleep(15)
        driver.get("https://www.iiuc.ac.bd/")
        driver.maximize_window()
        time.sleep(15)
        driver.close()


absc=runfirefox()
absc.firefoxx()