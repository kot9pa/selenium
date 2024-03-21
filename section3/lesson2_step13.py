import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):
    link1 = "https://suninjuly.github.io/registration1.html"
    link2 = "https://suninjuly.github.io/registration2.html"
        
    def __get_welcome_text(self, link):
        with webdriver.Chrome() as browser:
            browser.get(link)
            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first[required]")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second[required]")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third[required]")
            input3.send_keys("test@test")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            return welcome_text_elt.text

    def test_link1(self):
        self.assertEqual(self.__get_welcome_text(self.link1),
                         "Congratulations! You have successfully registered!",
                         )
        
    def test_link2(self):
        self.assertEqual(self.__get_welcome_text(self.link2), 
                         "Congratulations! You have successfully registered!",
                         )

if __name__ == "__main__":
    unittest.main()
