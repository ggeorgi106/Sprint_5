from selenium.webdriver.support.ui import WebDriverWait

from locators import Locators


def test_go_to_sauces_section(driver):
    sauces_tab = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(*Locators.SAUCES_TAB)
    )

    sauces_tab.click()

    WebDriverWait(driver, 10).until(
        lambda d: "tab_tab_type_current" in
        d.find_element(*Locators.SAUCES_TAB)
        .find_element("xpath", "..")
        .get_attribute("class")
    )

    assert "tab_tab_type_current" in driver.find_element(
        *Locators.SAUCES_TAB
    ).find_element(
        "xpath", ".."
    ).get_attribute("class")


def test_go_to_buns_section(driver):
    driver.find_element(*Locators.SAUCES_TAB).click()

    WebDriverWait(driver, 5).until(
        lambda d: "tab_tab_type_current" in
        d.find_element(*Locators.SAUCES_TAB)
        .find_element("xpath", "..")
        .get_attribute("class")
    )

    driver.find_element(*Locators.BUNS_TAB).click()

    WebDriverWait(driver, 5).until(
        lambda d: "tab_tab_type_current" in
        d.find_element(*Locators.BUNS_TAB)
        .find_element("xpath", "..")
        .get_attribute("class")
    )

    buns_tab = driver.find_element(*Locators.BUNS_TAB)
    assert "tab_tab_type_current" in buns_tab.find_element(
        "xpath", ".."
    ).get_attribute("class")


def test_go_to_fillings_section(driver):
    driver.find_element(*Locators.FILLINGS_TAB).click()

    WebDriverWait(driver, 5).until(
        lambda d: "tab_tab_type_current" in
        d.find_element(*Locators.FILLINGS_TAB)
        .find_element("xpath", "..")
        .get_attribute("class")
    )

    fillings_tab = driver.find_element(*Locators.FILLINGS_TAB)
    assert "tab_tab_type_current" in fillings_tab.find_element(
        "xpath", ".."
    ).get_attribute("class")