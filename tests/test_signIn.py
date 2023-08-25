# tests

from helpers.selenium_functions import * 

def test_signIn_success(browser):
    open_homepage(browser)
    navigate_to_login(browser)
    enter_email_and_pswd(browser)
    verify_user(browser)

def test_invalid_email(browser):
    open_homepage(browser)
    navigate_to_login(browser)
    enter_invalid_email(browser)

def test_invalid_pswd(browser):
    open_homepage(browser)
    navigate_to_login(browser)
    enter_invalid_pswd(browser)

def test_empty_email(browser):
    open_homepage(browser)
    navigate_to_login(browser)
    enter_empty_email(browser)

def test_empty_pswd(browser):
    open_homepage(browser)
    navigate_to_login(browser)
    enter_empty_pswd(browser)