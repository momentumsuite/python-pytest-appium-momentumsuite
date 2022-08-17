import pytest
import time
import json
from examples.pom_test.pages.androidPage import AndroidPage
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options

with open("test_settings.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

    cloudUser = jsonObject['CLOUD']['momentum.user']
    cloudToken = jsonObject['CLOUD']['momentum.token']
    cloudHost = jsonObject['CLOUD']['momentum.host']
    cloudAndroidApp = jsonObject['CLOUD']['android']['momentum.app']
    cloudRemoteDebugProxy = jsonObject['CLOUD']['remoteDebugProxy']
    cloudAndroidDeviceName = jsonObject['CLOUD']['android']['momentum.deviceList'][0]

    print(cloudHost)

options = UiAutomator2Options().load_capabilities({
'platformName': 'Android',
'appium:automationName': 'uiautomator2',
'appium:app': cloudAndroidApp,
'appium:autoGrantPermissions': True,
'appium:language': 'en',
'appium:locale': 'en',
'appium:fullReset': True,
'appium:noReset': False,
'appium:deviceName': '',
'appium:udid': '',
'appium.remoteDebugProxy': cloudRemoteDebugProxy,
'momentum:options': {
            'user': cloudUser,
            'token': cloudToken,
            'gw': cloudAndroidDeviceName,
        },
})

class TestPageObjectModel():

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Remote(cloudHost, options=options)
        driver.implicitly_wait(8)

        yield
        driver.quit()

    def test_pom(self, test_setup):
       AndroidPage.myFunction(driver, "first@mobven.com", "Pass321*")