from appium.webdriver.common.appiumby import AppiumBy


class LoginPageLocators:
    LOGIN_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/login")
    EMAIL_FIELD = (AppiumBy.ID, "com.ajaxsystems:id/login")
    PASSWORD_FIELD = (AppiumBy.ID, "com.ajaxsystems:id/password")
    SUBMIT_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/next")
    FORGOT_PASSWORD_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/forgot")


class MenuLocators:
    BURGER = (AppiumBy.ID, "com.ajaxsystems:id/menuDrawer")
    MENU = (AppiumBy.ID, "com.ajaxsystems:id/design_navigation_view")
    MENU_ADD_HUB_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/addHub")
    MENU_SETTINGS_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/settings")
    MENU_HELP_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/help")
    MENU_REPORT_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/logs")
    MENU_SERVICE_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/documentation_text")


class AddHubPage:
    PAGE_TITLE = (AppiumBy.ID, "com.ajaxsystems:id/toolbarTitle")


class SettingsPage:
    PAGE_TITLE = (AppiumBy.ID, "com.ajaxsystems:id/toolbarTitle")


class HelpPage:
    PAGE_TITLE = (AppiumBy.ID, "com.ajaxsystems:id/toolbarTitle")


class ReportPage:
    PAGE_TITLE = (AppiumBy.ID, "com.ajaxsystems:id/title")


class TermsPage:
    PAGE_TITLE = (AppiumBy.ID, "com.ajaxsystems:id/toolbarTitle")
