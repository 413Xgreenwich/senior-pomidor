from pages.base_page import BasePage
import time

class CheckoutComplete(BasePage):
    BACK_HOME_BUTTON_SELECTOR = '[id="back-to-products"]'
    BURGER_MENU_SELECTOR = '[id="react-burger-menu-btn"]'
    LOGOUT_BUTTON_SELECTOR = '[data-test="logout-sidebar-link"]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-complete.html'

    def go_back_home(self):
        self.wait_for_selector_and_click(self.BACK_HOME_BUTTON_SELECTOR)
    def logout(self):
        self.wait_for_selector_and_click(self.BURGER_MENU_SELECTOR)
        self.wait_for_selector_and_click(self.LOGOUT_BUTTON_SELECTOR)

