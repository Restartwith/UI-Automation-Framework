from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_add_item_to_cart(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_first_item_to_cart()

    assert inventory_page.get_cart_badge_count() == "1"
