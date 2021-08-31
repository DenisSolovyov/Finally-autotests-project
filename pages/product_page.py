from pages.main_page import MainPage
from pages.locators import ProductPageLocators


class ProductPage(MainPage):

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.GET_PRODUCT), "Login form is not presented"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.GET_PRODUCT).click()

    def get_basket_coast(self):
        self.coast = self.browser.find_element(*ProductPageLocators.BASKET_COAST).text




