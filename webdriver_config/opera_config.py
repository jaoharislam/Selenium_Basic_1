from selenium import webdriver

class Opera():
    def opera(self):
        driver = webdriver.Opera(executable_path="E:\\Drivers\\operadriver.exe")
        driver.get("http://www.iiuc.ac.bd")



abd=Opera()
abd.opera()