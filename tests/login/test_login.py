import time
import pytest
import logging

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "login, password, expected",
    [
        pytest.param(
            "test_login",
            "qa_automation_password",
            False,
            id="Login is incorrect",
        ),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "test_password",
            False,
            id="Password is incorrect",
        ),
        pytest.param(
            "test_login",
            "test_password",
            False,
            id="All credentials are incorrect"
        ),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            True,
            id="All credentials are valid",
        ),
    ],
)
def test_user_login(user_login_fixture, login, password, expected):
    page = user_login_fixture
    LOGGER.info(f"Start login test with login:{login} password:{password}")
    start = time.perf_counter()
    page.fill_credentials(login, password)
    end = time.perf_counter()
    LOGGER.info(f"It took: {round((end - start), 2)} seconds")
    page.wait(5)
    assert page.check_main_page() == expected
