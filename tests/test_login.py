from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators
from helpers import register_user
from data import BASE_URL


class TestLogin:

    def test_login_from_main_page(self, driver):
        email, password = register_user(driver)

        driver.get(BASE_URL)

        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/login")
        )

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL

    def test_login_from_personal_account(self, driver):
        email, password = register_user(driver)

        driver.get(BASE_URL)

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/login")
        )

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL

    def test_login_from_registration_form(self, driver):
        email, password = register_user(driver)

        driver.get(BASE_URL + "register")

        driver.find_element(*Locators.LOGIN_LINK).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/login")
        )

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL

    def test_login_from_forgot_password_form(self, driver):
        email, password = register_user(driver)

        driver.get(BASE_URL + "forgot-password")

        driver.find_element(*Locators.LOGIN_FROM_FORGOT_PASSWORD_LINK).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/login")
        )

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL