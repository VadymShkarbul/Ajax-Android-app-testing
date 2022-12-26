from framework.page import Page

LOGIN = "com.ajaxsystems:id/login"
PASS = "com.ajaxsystems:id/password"
LOGIN_BTN = "com.ajaxsystems:id/next"


class LoginPage(Page):
    def fill_credentials(self, login, password):
        self.fill_field(LOGIN, login)
        self.fill_field(PASS, password)
        self.click_element(LOGIN_BTN)
