# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # remove if you want to see the browser
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
