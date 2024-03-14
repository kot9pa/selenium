import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
  browser.get(link)

  firstname = browser.find_element(By.NAME, "firstname")
  firstname.send_keys("Ivan")

  lastname = browser.find_element(By.NAME, "lastname")
  lastname.send_keys("Petrov")

  email = browser.find_element(By.NAME, "email")
  email.send_keys("test@test")

  input_file = browser.find_element(By.CSS_SELECTOR, "[type='file']")
  
  with open('file.txt', 'w') as fp:
    #current_dir = os.path.dirname(__file__)
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, fp.name)
  
  input_file.send_keys(file_path)

  button = browser.find_element(By.XPATH, "//button[text()='Submit']")
  button.click()
finally:  
  time.sleep(5)
  browser.quit()
