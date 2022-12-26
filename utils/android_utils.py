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
        "udid": "emulator-5554",
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
    }
