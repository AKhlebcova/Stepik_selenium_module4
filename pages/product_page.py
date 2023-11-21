from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import ProductLocator


class ProductPage(BasePage):
    def should_be_added(self):
        self.should_be_add_to_basket()
        self.should_add_to_basket()
        self.should_see_success_adding_msg()
        self.should_see_basket_price_msg()
        self.should_see_benefit_applying_msg()
        self.should_be_right_price_in_msg()
        self.should_be_right_product_name_msg()

    def get_price(self):
        return self.browser.find_element(*ProductLocator.PRODUCT_PRICE).text

    def get_name(self):
        return self.browser.find_element(*ProductLocator.PRODUCT_NAME).text

    def should_be_add_to_basket(self):
        add_button = self.browser.find_elements(*ProductLocator.ADD_PRODUCT)
        assert self.is_element_present(*ProductLocator.ADD_PRODUCT), "There is no add button on current page"

    def should_add_to_basket(self):
        add_button = WebDriverWait(self.browser, 5).until(
        EC.element_to_be_clickable(ProductLocator.ADD_PRODUCT)
    )
        add_button.click()
        alert_text = self.solve_quiz_and_get_code()
        assert "Поздравляем, вы справились!" in alert_text, "Your attempt to add the product was failed"
    #
    def should_see_success_adding_msg(self):
        assert self.is_element_present(*ProductLocator.ALERT_NAME), "There is no message about adding of product"

    def should_see_basket_price_msg(self):
        assert self.is_element_present(*ProductLocator.ALERT_PRICE), "There is no message about basket price"

    def should_see_benefit_applying_msg(self):
        assert self.is_element_present(*ProductLocator.ALERT_OFFER_APPLIED), "There is no message about offer applying"

    def should_be_right_price_in_msg(self):
        alert_price = self.browser.find_element(*ProductLocator.ALERT_PRICE).text
        # right_price = self.browser.find_element(*ProductLocator.PRODUCT_PRICE).text
        assert alert_price == self.get_price(), "The price in alert is not equal to real price"

    def should_be_right_product_name_msg(self):
        alert_name = self.browser.find_element(*ProductLocator.ALERT_NAME).text
        # product_name = self.browser.find_element(*ProductLocator.PRODUCT_NAME).text
        assert alert_name == self.get_name(), "The name of the product and name in alert are not the same"




