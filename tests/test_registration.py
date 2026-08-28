from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators
from data import generate_email, generate_password


class TestRegistration:

    def test_successful_registration(self, driver):
        email = generate_email()
        password = generate_password()

        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/login")
        )

        driver.find_element(*Locators.REGISTER_LINK).click()

        driver.find_element(*Locators.NAME_INPUT).send_keys("Georgiy")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/login")
        )

        assert "/login" in driver.current_url

    def test_registration_with_invalid_password(self, driver):
        email = generate_email()

        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/login")
        )

        driver.find_element(*Locators.REGISTER_LINK).click()

        driver.find_element(*Locators.NAME_INPUT).send_keys("Georgiy")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("12345")

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        error = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                Locators.PASSWORD_ERROR
            )
        )

        assert error.text == "Некорректный пароль"