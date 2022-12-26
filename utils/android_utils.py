import subprocess


def get_device_uuid():
    devices = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    if devices:
        return devices.stdout.split()[4]
    else:
        raise Exception("No active devices")


def android_get_desired_capabilities():
    return {
        "autoGrantPermissions": True,
        "automationName": "uiautomator2",
        "newCommandTimeout": 500,
        "noSign": True,
        "platformName": "Android",
        "platformVersion": "11",
        "resetKeyboard": True,
        "systemPort": 8202,
        "takesScreenshot": True,
        "udid": get_device_uuid(),
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
    }
