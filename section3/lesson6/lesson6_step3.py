import pytest
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

'''
В @pytest.mark.parametrize() нужно передать параметр, 
который должен изменяться, и список значений параметра. 
В самом тесте наш параметр тоже нужно передавать в качестве аргумента.

Можно задавать параметризацию также для всего тестового класса, 
чтобы все тесты в классе запустились с заданными параметрами.
'''

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
