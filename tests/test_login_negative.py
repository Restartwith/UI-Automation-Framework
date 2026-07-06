from pages.login_page import LoginPage


def test_login_with_locked_out_user_shows_error(driver):
    login_page = LoginPage(driver)
    login_page.open().login("locked_out_user", "secret_sauce")

    assert "locked out" in login_page.get_error_message().lower()
