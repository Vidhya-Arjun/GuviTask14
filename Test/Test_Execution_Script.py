import pdb
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM.HomePage import HomePage
from POM.LoginPage import LoginPage


def test_valid_login(start_browser):
    driver  = start_browser
    home = HomePage(driver)
    home.launch_page()
    print("title launch ", driver.title)
    home.Set_Username("vidhyasarjun@gmail.com")
    home.Set_Password("hfdgfdkhlkf")


    cookies = driver.get_cookies()
    session_cookies = []
    print(cookies)
    for cookie in cookies:
        cookie_name = cookie['domain'].lower()
        if 'zenclass' in cookie_name:
            session_cookies.append(cookie)
    print(session_cookies)

    home.click_login()

    assert len(session_cookies) >0 ,"User not authenticated"

def test_invalid_login(start_browser):
    driver  = start_browser
    home = HomePage(driver)
    home.launch_page()
    print("title launch ", driver.title)
    home.Set_Username("vidhyasarjun@gmail.com")
    home.Set_Password("NHGFFFFFfugh")

    assert driver.current_url == "https://www.zenclass.in/login", "Invalid scenario, login should not happen"

def test_input_field_validation(start_browser):
    driver = start_browser
    home = HomePage(driver)
    home.launch_page()

    assert home.Get_Username().is_enabled(), "Username field not visible"
    assert home.Get_Password().is_enabled(), "Password field not visible"

def test_submit_button_validation(start_browser):
    driver = start_browser
    home = HomePage(driver)
    home.launch_page()

    home.Set_Username("vidhyasarjun@gmail.com")
    home.Set_Password("dsasgg")
    home.click_login()

    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']"))) -- not working

    assert driver.current_url =="https://www.zenclass.in/dashboard" , "login button validation failed"


def test_logout_button_validation(start_browser):
    driver = start_browser
    home = HomePage(driver)
    home.launch_page()
    home.Set_Username("vidhyasarjun@gmail.com")
    home.Set_Password("Guvi!2Plat")
    home.click_login()
    driver.get("https://www.zenclass.in/dashboard")


    login = LoginPage(driver)
    login.popup_close()
    login.User_icon_click()
    login.logout_click()

    assert driver.current_url=="https://www.zenclass.in/login", "Logout button validation failed"



