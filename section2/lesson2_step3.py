import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()

def calc(a, b):
  return str(sum([int(a), int(b)]))

try:    
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    result = calc(num1, num2)

    time.sleep(1)

    answer = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    answer.select_by_visible_text(result)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
