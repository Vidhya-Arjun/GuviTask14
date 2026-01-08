from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver



@pytest.fixture(scope="function")
def start_browser():
    options = Options()
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    yield driver
    driver.quit()



