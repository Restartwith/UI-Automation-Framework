from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username, password):
        username_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )

        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        login_button.click()
        return self

    def get_error_message(self):
        error = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        return error.text
