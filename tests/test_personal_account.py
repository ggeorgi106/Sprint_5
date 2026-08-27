from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators
from helpers import register_user
from data import BASE_URL


class TestPersonalAccount:

    def test_go_to_personal_account(self, driver):
        email, password = register_user(driver)

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(BASE_URL)
        )

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/account")
        )

        assert "/account" in driver.current_url

    def test_go_from_personal_account_to_constructor(self, driver):
        email, password = register_user(driver)

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(BASE_URL)
        )

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/account")
        )

        driver.find_element(*Locators.CONSTRUCTOR_LINK).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL

    def test_go_from_personal_account_to_constructor_by_logo(self, driver):
        email, password = register_user(driver)

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(BASE_URL)
        )

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/account")
        )

        driver.find_element(*Locators.LOGO_LINK).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL