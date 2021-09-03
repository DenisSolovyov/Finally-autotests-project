from pages.base_page import BasePage
from pages.locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_text_basket_empty(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_TEXT), "'Your basket is empty' is not presented"

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), "Items present in basket"
