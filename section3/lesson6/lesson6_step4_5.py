import math
import time
import os
import pytest
from contextlib import suppress
from dotenv import load_dotenv
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

if load_dotenv():
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")

auth_link = "https://stepik.org/lesson/236895/step/1"
lesson_ids = ["236895", "236896", "236897", 
              "236898", "236899",  "236903", 
              "236904", "236905"]

class TestStep5():
    hints = ""

    def test_stepik_basic_authorize(self, browser: WebDriver):
        browser.get(auth_link)
        login_button = browser.find_element(By.CLASS_NAME, "navbar__auth_login")
        login_button.click()    
        
        email_input = browser.find_element(By.ID, "id_login_email")
        email_input.send_keys(login)
        password_input = browser.find_element(By.ID, "id_login_password")
        password_input.send_keys(password)
        submit_button = browser.find_element(By.CLASS_NAME, "sign-form__btn")
        submit_button.click()

        time.sleep(1) # ждем когда модальное окно авторизации закроется
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CLASS_NAME, "auth-modal")
            pytest.fail("Не должно быть auth-modal")

    @classmethod
    @pytest.mark.parametrize("lesson", lesson_ids)    
    def test_parametrisation(cls, browser: WebDriver, lesson):
        wait = WebDriverWait(browser, 3)
        lesson_link = f"https://stepik.org/lesson/{lesson}/step/1"
        browser.get(lesson_link)

        with suppress(NoSuchElementException, TimeoutException):
            again_btn = browser.find_element(By.CLASS_NAME, "again-btn")
            again_btn.click()
            confirm_btn = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".modal-popup__footer>button:nth-child(1)")))
            confirm_btn.click()

        textarea = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")        
        textarea.send_keys(cls.__get_answer())

        submit_button = wait.until(EC.element_to_be_clickable(
               (By.CLASS_NAME, "submit-submission")))
        submit_button.click()

        result = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        try:
            assert result.text == "Correct!"
        except AssertionError:
            cls.hints += result.text

    @classmethod
    def test_print_smart_hints(cls):
        print("\n\nAnswer =", cls.hints)

    @staticmethod
    def __get_answer():
        return math.log(int(time.time()))
    
if __name__ == "__main__":
    pytest.main()
