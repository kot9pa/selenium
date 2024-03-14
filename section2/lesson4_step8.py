import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button1 = browser.find_element(By.ID, "book")
    button1.click()

    time.sleep(1)
    input_value = browser.find_element(By.ID, "input_value")
    x = input_value.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    button2 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button2.click()
finally:
    time.sleep(5)
    browser.quit()   
