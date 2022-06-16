import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AndroidPage():

    def myFunction(driver, username, password):
        elUsername = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ID, "username_txt")))
        elUsername.send_keys(username)

        elPassword = driver.find_element(by=AppiumBy.ID, value="password_txt")
        elPassword.send_keys(password)

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