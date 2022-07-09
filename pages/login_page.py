from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.find("login") != -1, "The url is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "There is no login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTR_USERNAME), "There is no login formThere is no registration form on the page"

    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*LoginPageLocators.EMAIL_REG)
        user_email.send_keys(email)
        user_password = self.browser.find_element(*LoginPageLocators.PASSWORD_REG)
        user_password.send_keys(password)
        conf_user_password = self.browser.find_element(*LoginPageLocators.CONF_PASSWORD_REG)
        conf_user_password.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        register_button.click()
