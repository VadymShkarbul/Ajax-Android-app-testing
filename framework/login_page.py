from framework.page import Page
from framework.locators import LoginPageLocators, MenuLocators


class LoginPage(Page):
    def fill_credentials(self, login, password):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        self.fill_text_field(LoginPageLocators.EMAIL_FIELD, login)
        self.fill_text_field(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_element(LoginPageLocators.SUBMIT_BUTTON)

    def check_main_page(self):
        return self.check_element(MenuLocators.BURGER)
