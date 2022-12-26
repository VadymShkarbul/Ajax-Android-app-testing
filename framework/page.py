from appium.webdriver import WebElement
from selenium.common import NoSuchElementException


class Page:
    def __init__(self, driver):
        self.driver = driver

    def check_element(self, locator: tuple) -> bool:
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        else:
            return True

    def find_element(self, locator: tuple) -> WebElement:
        if not self.check_element(locator):
            raise NoSuchElementException(f"Element with ID:{locator[1]} does not exist")
        return self.driver.find_element(*locator)

    def click_element(self, locator: tuple) -> None:
        element = self.find_element(locator)
        element.click()

    def fill_text_field(self, locator: tuple, keys: str) -> None:
        field = self.find_element(locator)
        field.send_keys(keys)

    def wait(self, seconds: int) -> None:
        self.driver.implicitly_wait(seconds)

    def go_back(self) -> None:
        self.driver.back()
