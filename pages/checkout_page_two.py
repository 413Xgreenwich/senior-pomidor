from pages.base_page import BasePage


class CheckoutPageTwo(BasePage):
    FINISH_BUTTON_SELECTOR = '[id="finish"]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-step-two.html'

    def finish_checkout(self):
        self.wait_for_selector_and_click(self.FINISH_BUTTON_SELECTOR)
