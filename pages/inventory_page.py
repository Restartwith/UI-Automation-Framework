from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")
        return self

    def add_first_item_to_cart(self):
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test^='add-to-cart']"))
        )
        add_button.click()
        return self

    def get_cart_badge_count(self):
        badge = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        return badge.text
