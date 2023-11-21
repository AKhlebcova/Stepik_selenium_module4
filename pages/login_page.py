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
        login_form = self.browser.find_elements(*LoginPageLocators.LOGIN_FORM)
        assert len(login_form) > 0, "The page doesn't contain login form"

    def should_be_register_form(self):
        registration_form = self.browser.find_elements(*LoginPageLocators.REGISTER_FORM)
        assert len(registration_form) > 0, "The page doesn't contain registration form"
