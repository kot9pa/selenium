import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

'''
После завершения теста, который вызывал фикстуру, 
выполнение фикстуры продолжится со строки, следующей за строкой со словом yield

Для фикстур можно задавать область покрытия фикстур (scope). 
Допустимые значения: “function”, “class”, “module”, “session”. 
Соответственно, фикстура будет вызываться один раз для тестового метода, 
один раз для класса, один раз для модуля или один раз для всех тестов, 
запущенных в данной сессии

При описании фикстуры можно указать дополнительный параметр autouse=True, 
который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова
'''

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    yield driver
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    driver.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print("\npreparing some critical data for every test")

class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")
