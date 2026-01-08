import pytest
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Baseclass:
    def __init__(self,driver,timeout =10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,timeout)

    def defining_locator(self,locator):
       try:
            return self.wait.until(EC.presence_of_element_located(locator))
       except TimeoutException:
            pytest.fail("Element not located")



