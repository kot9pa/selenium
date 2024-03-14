import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.execute_script("window.scrollBy(0, 100);")
button.click()

time.sleep(10)