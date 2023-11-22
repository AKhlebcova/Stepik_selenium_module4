from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_FORM_SECRETKEY1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTER_FORM_SECRETKEY2 = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    REGISTER_FORM_ERROR_MSG = (By.CSS_SELECTOR, ".alert.alert-danger")


class ProductPageLocators():
    ADD_PRODUCT = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    ALERT_NAME = (By.CSS_SELECTOR, "#messages div:first-child > .alertinner > strong")
    ALERT_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    ALERT_OFFER_APPLIED = (By.CSS_SELECTOR, "#messages div:nth-child(2)	> .alertinner > strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn.btn-default[href$="basket/"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, '#content_inner > .basket-title')
