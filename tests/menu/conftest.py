import pytest

from framework.menu_page import MenuPage


@pytest.fixture(scope="function")
def user_login_fixture(driver):
    yield MenuPage(driver)
