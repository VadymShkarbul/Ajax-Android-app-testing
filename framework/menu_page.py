from framework.page import Page

BURGER = "com.ajaxsystems:id/menuDrawer"


class MenuPage(Page):
    def burger_click(self):
        return self.click_element(BURGER)