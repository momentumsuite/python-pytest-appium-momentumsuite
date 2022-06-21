import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC


class IosPage():

    def myFunction(driver):
        

        elOne = driver.find_element(by=AppiumBy.XPATH, value="(//*[contains(@label , '2')])[1]")
        elOne.click()

        elTwo = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@name='+']")
        elTwo.click()

        elThree = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@name='5']")
        elThree.click()


        elFour = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@name='=']")
        elFour.click()

        time.sleep(3)


        total = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@name='7']")

        if total!=None and total.text=="7":
            assert True
        else:
            assert False