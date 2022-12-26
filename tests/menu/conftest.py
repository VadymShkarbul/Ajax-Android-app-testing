import time
import pytest

from framework.login_page import LoginPage
from framework.menu_page import MenuPage


@pytest.fixture(scope="session")
def user_login_fixture(driver):
    driver.launch_app()
    page = LoginPage(driver)
    page.fill_credentials("qa.ajax.app.automation@gmail.com", "qa_automation_password")
    time.sleep(5)


@pytest.fixture(scope="function")
def menu_fixture(user_login_fixture, driver):
    yield MenuPage(driver)
