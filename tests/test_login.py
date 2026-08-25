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


def test_login_from_main_page(driver):
    email, password = register_user(driver)

    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_contains("/login")
    )

    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_to_be(
            "https://stellarburgers.education-services.ru/"
        )
    )

    assert driver.current_url == "https://stellarburgers.education-services.ru/"


def test_login_from_personal_account(driver):
    email, password = register_user(driver)

    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_contains("/login")
    )

    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_to_be(
            "https://stellarburgers.education-services.ru/"
        )
    )

    assert driver.current_url == "https://stellarburgers.education-services.ru/"


def test_login_from_registration_form(driver):
    email, password = register_user(driver)

    driver.get("https://stellarburgers.education-services.ru/register")

    driver.find_element(*Locators.LOGIN_LINK).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_contains("/login")
    )

    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_to_be(
            "https://stellarburgers.education-services.ru/"
        )
    )

    assert driver.current_url == "https://stellarburgers.education-services.ru/"


def test_login_from_forgot_password_form(driver):
    email, password = register_user(driver)

    driver.get("https://stellarburgers.education-services.ru/forgot-password")

    driver.find_element(*Locators.LOGIN_FROM_FORGOT_PASSWORD_LINK).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_contains("/login")
    )

    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_to_be(
            "https://stellarburgers.education-services.ru/"
        )
    )

    assert driver.current_url == "https://stellarburgers.education-services.ru/"