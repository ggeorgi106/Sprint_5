from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators
from helpers import register_user
from data import BASE_URL


class TestLogout:

    def test_logout_from_personal_account(self, driver):
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

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                Locators.LOGOUT_BUTTON
            )
        ).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/login")
        )

        assert "/login" in driver.current_url