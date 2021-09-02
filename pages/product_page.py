from pages.main_page import MainPage
from pages.locators import ProductPageLocators


class ProductPage(MainPage):

    def should_be_add_to_basket(self, ):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AT_HEAD).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_AT_BASKET).text, "Failed name: basket_name != head_name"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.GET_PRODUCT).click()

    def get_basket_coast(self):
        basket_coast = self.browser.find_element(*ProductPageLocators.BASKET_COAST).text
        return basket_coast

    def product_price_at_head(self):
        product_price_head = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price_head

    def product_name_at_basket(self):
        name_at_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AT_BASKET).text
        return name_at_basket

    def product_name_at_head(self):
        head_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AT_HEAD).text
        return head_name

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared, but should not be"
