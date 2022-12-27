import logging

import pytest

from framework.locators import (
    MenuLocators,
    AddHubPage,
    SettingsPage,
    HelpPage,
    ReportPage,
    TermsPage,
)

LOGGER = logging.getLogger(__name__)


def test_menu_open(menu_fixture):
    page = menu_fixture
    page.wait(5)
    page.menu_open()
    assert page.check_element(MenuLocators.MENU)


@pytest.mark.parametrize(
    "locator",
    [
        pytest.param(
            MenuLocators.MENU_ADD_HUB_BUTTON,
            id="'Add hub' menu item exist",
        ),
        pytest.param(
            MenuLocators.MENU_SETTINGS_BUTTON,
            id="'App Settings' menu item exist",
        ),
        pytest.param(
            MenuLocators.MENU_HELP_BUTTON,
            id="'Help' menu item exist",
        ),
        pytest.param(
            MenuLocators.MENU_REPORT_BUTTON,
            id="'Report a problem' menu item exist",
        ),
        pytest.param(
            MenuLocators.MENU_SERVICE_BUTTON,
            id="'Terms of Service' menu item exist",
        ),
    ],
)
def test_menu_buttons_enabled(menu_fixture, locator: tuple):
    page = menu_fixture
    if not page.check_element(MenuLocators.MENU):
        page.menu_open()
    assert page.check_element(locator)


@pytest.mark.parametrize(
    "button, locator, title",
    [
        pytest.param(
            MenuLocators.MENU_ADD_HUB_BUTTON,
            AddHubPage.PAGE_TITLE,
            "Add hub",
            id="Redirect to 'Add hub' page",
        ),
        pytest.param(
            MenuLocators.MENU_SETTINGS_BUTTON,
            SettingsPage.PAGE_TITLE,
            "Account",
            id="Redirect to 'App Settings' page",
        ),
        pytest.param(
            MenuLocators.MENU_HELP_BUTTON,
            HelpPage.PAGE_TITLE,
            "Installation Manuals",
            id="Redirect to 'List of devices manuals' page",
        ),
        pytest.param(
            MenuLocators.MENU_REPORT_BUTTON,
            ReportPage.PAGE_TITLE,
            "Report a problem",
            id="Redirect to 'List of devices manuals' page",
        ),
        pytest.param(
            MenuLocators.MENU_SERVICE_BUTTON,
            TermsPage.PAGE_TITLE,
            "Terms of Service",
            id="Redirect to 'Terms of Service' page",
        ),
    ],
)
def test_menu_buttons_click(menu_fixture, button, locator, title):
    page = menu_fixture
    if not page.check_element(MenuLocators.MENU):
        page.menu_open()
    page.click_element(button)
    assert page.get_page_title(locator) == title
    page.go_back()
