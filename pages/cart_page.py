from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/cart.html")
        return self

    def get_cart_item_count(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "cart_item"))

    def remove_first_item(self):
        remove_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test^='remove']"))
        )
        remove_button.click()
        return self

    def checkout(self):
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
        return self
