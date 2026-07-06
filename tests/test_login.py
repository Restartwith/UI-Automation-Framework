from pages.login_page import LoginPage


def test_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open().login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url
