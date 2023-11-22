from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_line = self.browser.current_url
        print(url_line)
        assert 'login' in url_line, "URL is not login-url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "The page doesn't contain login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "The page doesn't contain registration form"

    def register_new_user(self, email, password):
        email_el = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_el.send_keys(email)
        secret1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SECRETKEY1)
        secret1.send_keys(password)
        secret2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SECRETKEY2)
        secret2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON)
        button.click()
        assert self.is_not_element_present(
            *LoginPageLocators.REGISTER_FORM_ERROR_MSG), "Error message is present, but should not be"
