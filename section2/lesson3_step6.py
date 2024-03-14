import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link1 = "http://suninjuly.github.io/redirect_accept.html"
#link2 = "http://suninjuly.github.io/alert_redirect.html"
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def get_window():
  # skip first
  for window in browser.window_handles[1:]:
    yield window

try:
  browser.get(link1)
  button1 = browser.find_element(By.XPATH, "//button[@type='submit']")
  button1.click()

  time.sleep(1)

  browser.switch_to.window(next(get_window()))
  input_value = browser.find_element(By.ID, "input_value")
  x = input_value.text
  y = calc(x)

  answer = browser.find_element(By.ID, "answer")
  answer.send_keys(y)

  button2 = browser.find_element(By.XPATH, "//button[@type='submit']")
  button2.click()
finally:
  time.sleep(10)
  browser.quit()
