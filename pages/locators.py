from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_PRODUCT = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    ALERT_NAME = (By.CSS_SELECTOR, "#messages div:first-child > .alertinner > strong")
    ALERT_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    ALERT_OFFER_APPLIED = (By.CSS_SELECTOR, "#messages div:nth-child(2)	> .alertinner > strong")