import subprocess

import pytest
from appium import webdriver

from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope="session")
def run_appium_server():
    subprocess.Popen(
        ["appium", "-a", "0.0.0.0", "-p", "4723", "--allow-insecure", "adb_shell"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True,
    )
    time.sleep(5)


@pytest.fixture(scope="session")
def driver(run_appium_server):
    driver = webdriver.Remote(
        "http://localhost:4723/wd/hub", android_get_desired_capabilities()
    )
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def get_device_uuid():
    devices = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    return devices.stdout.split()[4]
