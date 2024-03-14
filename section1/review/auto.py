from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/registration2.html")
    #driver.get("http://suninjuly.github.io/registration1.html")

    first_name_input = driver.find_element("css selector", "input.first[required]")
    first_name_input.send_keys("Ivan")

    last_name_input = driver.find_element("css selector", "input.second[required]")
    last_name_input.send_keys("Petrov")

    email_input = driver.find_element("css selector", "input.third[required]")
    email_input.send_keys("nastya-odinokova@mail.ru")

    submit_button = driver.find_element("css selector", "button.btn-default")
    submit_button.click()

finally:
    time.sleep(30)
    driver.quit()
