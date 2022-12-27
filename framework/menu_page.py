from framework.locators import MenuLocators
from framework.page import Page


class MenuPage(Page):
    def menu_open(self) -> None:
        self.click_element(MenuLocators.BURGER)
