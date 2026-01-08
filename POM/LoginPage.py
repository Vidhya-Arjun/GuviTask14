from selenium.webdriver.common.by import By

from POM.Baseclass import Baseclass


class LoginPage(Baseclass):

    USERICON =(By.XPATH,"//img[@id='profile-click-icon']")
    LOGOUT =(By.XPATH,"//div[contains(text(),'Log out')]")
    POPUP =(By.XPATH,"//button[@aria-label='Close popup']")

    def __init__(self,driver,timeout=10):
        super().__init__(driver,timeout)
    def popup_close(self):
        self.defining_locator(self.POPUP).click()
    def User_icon_click(self):
        self.defining_locator(self.USERICON).click()
    def logout_click(self):
        self.defining_locator(self.LOGOUT).click()