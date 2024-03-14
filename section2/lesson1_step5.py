import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:    
    browser.get(link)    

    input_value = browser.find_element(By.ID, "input_value")
    x = input_value.text
    y = calc(x)

    time.sleep(1)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robots_rule = browser.find_element(By.ID, "robotsRule")
    robots_rule.click()

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
