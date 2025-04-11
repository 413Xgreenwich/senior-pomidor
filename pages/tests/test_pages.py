from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page_one import CheckoutPageOne
from pages.checkout_page_two import CheckoutPageTwo
from pages.checkout_complete import CheckoutComplete
import allure


@allure.title("Проверка критического пути проекта pages")
def test_add_items_and_checkout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page_one = CheckoutPageOne(page)
    checkout_page_two = CheckoutPageTwo(page)
    checkout_complete = CheckoutComplete(page)

    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_first_item_to_cart()
    checkout_page_one.start_checkout()
    checkout_page_one.fill_checkout_form("Alex", "Greenwich", "13373228")
    checkout_page_one.click_to_continue()
    checkout_page_two.finish_checkout()
    checkout_complete.go_back_home()
    checkout_complete.logout()
