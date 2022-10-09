from selenium import webdriver
from webdriver_manager.opera import OperaDriverManager
import opera
import Opera

options = webdriver.ChromeOptions()
options.add_argument('allow-elevated-browser')
options.binary_location = "C:\\Users\\dudae\\AppData\\Local\\Programs\\Opera\\opera.exe"
driver = webdriver.Opera(executable_path=OperaDriverManager().install(), options=options)
driver.maximize_window()
driver.get("https://www.youtube.com/")
title = driver.title
print(title)
