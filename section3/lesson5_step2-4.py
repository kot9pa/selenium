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

@pytest.fixture()
def browser():
    logging.info("Execute fixture")
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    yield driver
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    driver.quit()

@pytest.mark.usefixtures("browser")
class TestMainPage1():
    
    @pytest.mark.smoke
    @pytest.mark.win7
    @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
