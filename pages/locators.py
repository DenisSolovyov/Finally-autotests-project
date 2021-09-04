from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset > div")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")



class MainPageLocators:
    pass
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    GET_PRODUCT_BTN = None
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    CONF_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")




class ProductPageLocators:
    GET_PRODUCT = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BASKET_COAST = (
        By.CSS_SELECTOR,
        "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRODUCT_NAME_AT_HEAD = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRODUCT_NAME_AT_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

