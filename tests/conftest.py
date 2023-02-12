import pytest
from selenium import webdriver

url = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture
def driver():
    browser_driver = webdriver.Chrome()
    browser_driver.get(url)
    yield browser_driver
    browser_driver.quit()

