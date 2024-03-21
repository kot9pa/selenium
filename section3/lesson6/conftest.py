import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser():
    options = webdriver.ChromeOptions()
    #options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--headless") # Hide windows
    options.add_argument("--log-level=3") # Hide console logs
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
