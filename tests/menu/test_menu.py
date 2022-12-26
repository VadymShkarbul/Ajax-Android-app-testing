import time
import pytest


def test_menu(user_login_fixture):
    time.sleep(3)
    user_login_fixture.burger_click()
    assert user_login_fixture.find_element("com.ajaxsystems:id/logs").is_displayed() is True


@pytest.mark.parametrize(
    "locator, expected",
    [
        pytest.param(
            "com.ajaxsystems:id/addHub",
            True,
            id="Add hub menu item exist",
        ),
        pytest.param(
            "com.ajaxsystems:id/settings",
            True,
            id="Settings menu item exist",
        ),
        pytest.param(
            "com.ajaxsystems:id/help",
            True,
            id="Help menu item exist",
        ),
        pytest.param(
            "com.ajaxsystems:id/logs",
            True,
            id="Report menu item exist",
        ),
    ],
)
def test_menu_menu_items_exist(user_login_fixture, locator, expected):
    assert user_login_fixture.find_element(locator).is_displayed() is expected
