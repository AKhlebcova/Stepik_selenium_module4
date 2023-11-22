from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_msg(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MSG), "There is no message about empty basket"

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "Products are present, but they shouldn't"