from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators
from data import generate_email, generate_password


def register_user(driver):
    email = generate_email()
    password = generate_password()

    driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        expected_conditions.url_contains("/login")
    )

    driver.find_element(*Locators.REGISTER_LINK).click()

    driver.find_element(*Locators.NAME_INPUT).send_keys("Georgiy")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 20).until(
        expected_conditions.url_contains("/login")
    )

    return email, password