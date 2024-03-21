import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

'''
Мы можем маркировать небольшое количество критичных тестов (smoke), 
которые нужно запускать на каждый коммит разработчиков, 
а остальные тесты обозначить как регрессионные (regression) и 
запускать их только перед релизом

pytest -s -v -m <regression> название маркировки

Маркировать тесты можно не только для их фильтрации. 
А также, например, для передачи в тестовый класс, фикстуры уровня класса (scope="class"). 
Для этого используется @pytest.mark.usefixtures

Чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip
'''
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

'''
Чтобы результат прогона всех наших тестов был успешен, 
но падающий тест помечался соответствующим образом, чтобы про него не забыть. 
Добавим маркировку @pytest.mark.xfail для падающего теста

'''
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        #browser.find_element(By.CSS_SELECTOR, "button.favorite") # bug
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")
