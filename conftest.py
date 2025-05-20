from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()