from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_remove_item_from_cart(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")

    InventoryPage(driver).add_first_item_to_cart()

    cart_page = CartPage(driver)
    cart_page.open().remove_first_item()

    assert cart_page.get_cart_item_count() == 0
