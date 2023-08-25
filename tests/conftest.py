# conftest.py

import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()  # Adjust the path accordingly
    yield driver
    driver.quit()
