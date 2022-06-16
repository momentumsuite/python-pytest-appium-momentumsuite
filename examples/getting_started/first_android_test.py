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
    cloudAndroidApp = jsonObject['CLOUD']['android']['momentum.app']
    cloudAndroidDeviceName = jsonObject['CLOUD']['android']['momentum.deviceList'][0]
    print(cloudHost)

desired_caps = {
    "platformName": "Android",
    "appium:automationName": "uiautomator2",
    "momentum:user": cloudUser,
    "momentum:token": cloudToken,
    "momentum:gw": cloudAndroidDeviceName,
    "appium:app": cloudAndroidApp,
    "appium:autoGrantPermissions": True,
    "appium:language": "en",
    "appium:locale": "en",
    "appium:fullReset": True,
    "appium:noReset": False,
    "appium:deviceName": "",
    "appium:udid": ""
}

driver = webdriver.Remote(cloudHost, desired_caps)

def test_first_android():
  elUsername = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ID, "username_txt")))
  elUsername.send_keys("first@mobven.com")

  elPassword = driver.find_element(by=AppiumBy.ID, value="password_txt")
  elPassword.send_keys("Pass321*")

  elSubmit = driver.find_element(by=AppiumBy.ID, value="login_btn")
  elSubmit.click()

  time.sleep(3)

  is_account_visible = driver.find_element(by=AppiumBy.ID, value="account_layout").is_displayed()
  assert(is_account_visible)

  elBalance = driver.find_element(by=AppiumBy.ID, value="balance_txt")

  if elBalance!=None and elBalance.text=="1000000":
    assert True
  else:
    assert False

  driver.quit()