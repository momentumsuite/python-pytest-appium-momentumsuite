import pytest
import json
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with open("test_settings.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

    cloudUser = jsonObject['CLOUD']['momentum.user']
    cloudToken = jsonObject['CLOUD']['momentum.token']
    cloudHost = jsonObject['CLOUD']['momentum.host']
    cloudIosApp = jsonObject['CLOUD']['ios']['momentum.app']
    cloudIosDeviceName = jsonObject['CLOUD']['ios']['momentum.deviceList'][0]
    print(cloudHost)

desired_caps = {
    "platformName": "iOS",
    "appium:automationName": "XCUITest",
    "momentum:user": cloudUser,
    "momentum:token": cloudToken,
    "momentum:gw": cloudIosDeviceName,
    "appium:app": cloudIosApp,
    "appium:autoAcceptAlerts": True,
    "appium:language": "en",
    "appium:locale": "en",
    "appium:fullReset": True,
    "appium:noReset": False,
    "appium:deviceName": "",
    "appium:udid": ""
}

driver = webdriver.Remote(cloudHost, desired_caps)

def test_first_ios():
  elOne = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, "(//*[contains(@label , '2')])[1]")))
  elOne.click()

  elTwo = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@name='+']")
  elTwo.click()

  elThree = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@name='5']")
  elThree.click()

  elFour = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@name='=']")
  elFour.click()

  time.sleep(3)

  driver.quit()