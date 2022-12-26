from appium.webdriver.common.appiumby import AppiumBy


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: str):
        return self.driver.find_element(AppiumBy.ID, locator)

    def click_element(self, locator: str):
        return self.driver.find_element(AppiumBy.ID, locator).click()

    def fill_field(self, locator: str, keys: str):
        field = self.find_element(locator)
        field.click()
        field.send_keys(keys)
        return field
