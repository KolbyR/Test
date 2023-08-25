# Selenium Functions
from config import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_homepage(browser):
    browser.get("https://hudl.com")
    assert browser.title == "Hudl • Tools to help every team, coach and athlete improve"


def navigate_to_login(browser):
    drop_down = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "body > div.outer > header > div > div > a > svg")
        )
    )
    drop_down.click()
    hudl = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "body > div.outer > header > div > div > div > div > div:nth-child(1) > div > a",
            )
        )
    )
    hudl.click()
    assert browser.title == "Log In"


def enter_email_and_pswd(browser):
    email = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email.send_keys(user_email)
    pswd = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    pswd.send_keys(user_pswd)
    log_in = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "logIn"))
    )
    log_in.click()
    WebDriverWait(browser, 10).until(EC.title_is("Home - Hudl"))
    assert browser.title == "Home - Hudl"


def verify_user(browser):
    user_name = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "hui-globaluseritem__display-name")
        )
    )
    assert user_name.text == "Kolby R"


def enter_invalid_email(browser):
    email = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email.send_keys("xyz@gmail.com")
    pswd = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    pswd.send_keys(user_pswd)
    log_in = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "logIn"))
    )
    log_in.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "uni-notice__content"))
    )
    signIn_error = browser.find_element(
        By.CSS_SELECTOR,
        ".uni-notice__content .error-message.uni-text.uni-text--small.uni-text--set-solid",
    )
    assert signIn_error.text == "We don't recognize that email and/or password"
    assert browser.title == "Log In"


def enter_invalid_pswd(browser):
    email = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email.send_keys(user_email)
    pswd = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    pswd.send_keys("KX123byz")
    log_in = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "logIn"))
    )
    log_in.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "uni-notice__content"))
    )
    signIn_error = browser.find_element(
        By.CSS_SELECTOR,
        ".uni-notice__content .error-message.uni-text.uni-text--small.uni-text--set-solid",
    )
    assert signIn_error.text == "We don't recognize that email and/or password"
    assert browser.title == "Log In"


def enter_empty_pswd(browser):
    email = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email.send_keys(user_email)
    log_in = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "logIn"))
    )
    log_in.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "uni-notice__content"))
    )
    signIn_error = browser.find_element(
        By.CSS_SELECTOR,
        ".uni-notice__content .error-message.uni-text.uni-text--small.uni-text--set-solid",
    )
    assert signIn_error.text == "Please fill in all of the required fields"
    assert browser.title == "Log In"


def enter_empty_email(browser):
    pswd = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    pswd.send_keys(user_pswd)
    log_in = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "logIn"))
    )
    log_in = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "logIn"))
    )
    log_in.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "uni-notice__content"))
    )
    signIn_error = browser.find_element(
        By.CSS_SELECTOR,
        ".uni-notice__content .error-message.uni-text.uni-text--small.uni-text--set-solid",
    )
    assert signIn_error.text == "Please fill in all of the required fields"
    assert browser.title == "Log In"
