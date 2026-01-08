from selenium.webdriver.common.by import By

from POM.Baseclass import Baseclass


class HomePage(Baseclass):

    USERNAMEINPUT =(By.XPATH,"//input[@placeholder='Enter your mail']")
    PASSWORDINPUT =(By.XPATH,"//input[@type='password']")
    LOGINBUTTON = (By.XPATH,"//button[@type='submit']")
    URLINPUT = "https://www.zenclass.in/"

    def __init__(self,driver,timeout=10):
        super().__init__(driver,timeout)
    def launch_page(self):
        self.driver.get(self.URLINPUT)
    def Get_Username(self):
        return self.defining_locator(self.USERNAMEINPUT)
    def Get_Password(self):
        return self.defining_locator(self.PASSWORDINPUT)
    def Set_Username(self,username):
        self.Get_Username().clear()
        self.Get_Username().send_keys(username)
    def Set_Password(self,password):
        self.Get_Password().clear()
        self.Get_Password().send_keys(password)
    def click_login(self):
        self.defining_locator(self.LOGINBUTTON).click()

