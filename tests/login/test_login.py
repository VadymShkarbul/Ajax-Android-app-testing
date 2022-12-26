import time

import pytest
import logging

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "login, password, locator, expected",
    [
        pytest.param(
            "test",
            "qa_automation_password",
            "com.ajaxsystems:id/forgot",
            True,
            id="Login is incorrect",
        ),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "test",
            "com.ajaxsystems:id/forgot",
            True,
            id="Password is incorrect"),
        pytest.param(
            "test",
            "test",
            "com.ajaxsystems:id/forgot",
            True,
            id="All credentials are incorrect"),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            "com.ajaxsystems:id/icNoHub",
            True,
            id="All credentials are valid"
        ),
    ],
)
def test_user_login(user_login_fixture, login, password, locator, expected):
    user_login_fixture.click_element("com.ajaxsystems:id/login")
    time.sleep(3)

    LOGGER.info("Start enter credentials...")
    start = time.perf_counter()
    user_login_fixture.fill_credentials(login, password)
    end = time.perf_counter()
    LOGGER.info(f"It took: {round((end - start), 2)} seconds")

    time.sleep(3)

    assert user_login_fixture.find_element(locator).is_displayed() is expected

    LOGGER.info(f"Finished!")


def test_getting_uuid(get_device_uuid):
    LOGGER.info("Check device uuid")
    assert get_device_uuid == "emulator-5554"
