# Python PyTest Appium Momentumsuite

![image](https://user-images.githubusercontent.com/105457661/174085415-9e1e7d8e-da2b-41ab-9099-773d3170d4fc.png)
[PyTest](https://docs.pytest.org/) Integration with local or [Momentum Suite](https://www.momentumsuite.com/) real mobile farm devices

## Supports
  * Selenium v4 and Appium 2.0 (W3C)
  * Native or Hybrid Android and iOS apps (APK, AAB, IPA)
  * Page Object Model (POM) usage with [pytest](https://docs.pytest.org/)
  * Local testing or using Momentum Suite's 150+ Android or iOS devices
  * Auto generated HTML [Allure](https://docs.qameta.io/allure/) test report after test

## Setup

**Requirements:**

* [Python](https://www.python.org/downloads/) version 3.7+ (required by [Appium Python Client](https://github.com/appium/python-client) v2.2 and pytest)
* Install the [Allure command-line tool](https://www.npmjs.com/package/allure-commandline) (required to process the results directory after test run)

**Install the dependencies:**

Run the following command in project's base directory :
```
pip3 install -r requirements.txt
```

## Getting Started
Getting Started with Appium tests using Python PyTest on Momentum Suite couldn't be easier!
With a Momentum Suite account, You need 4 things to start without any Appium or Android SDK dependencies.
  * **momentum:user** Usually it could be your email address
  * **momentum:token** Your unique access token learned from momentumsuite.com
  * **momentum:gw** Comma seperated Momentum Suite mobile device ID list (4 digit number) to run the test. First number will be your default phone for all except parallel-testing.
  * **appium:app** Your uploaded IPA, APK or AAB app file from Momentum Suite Application Library. Example format is ms://<hashed-app-id> Optionally you can use a public accessible web URL.
 
 Do not forget to set these 4 Appium capability values and check hostname, port, path and protocol values on your **test_settings.json** file.
  
  
### Start with Android device:
 
 Open for editing your test_settings.json file under [root directory](https://github.com/momentumsuite/python-pytest-appium-momentumsuite/tree/main/test_settings.json).
 
 Set momentum.user, momentum.token, momentum.deviceList, momentum.app on test_settings.json file.
 
 Test script is available in getting_started directory
 
 Run the following command in project's base directory :
```
python3 -m pytest examples/getting_started/first_android_test.py --alluredir=allure_results
```


### Start with iOS device:
 
Same with Android, but need to change test_settings.json file.
 
Run the following command in project's base directory :
```
python3 -m pytest examples/getting_started/first_ios_test.py --alluredir=allure_results
```
 

### Start with local testing:
 
Use Local testing that access resources hosted in your development or testing environments. You need to install Appium and it's all dependencies like Android SDK, Xcode, Command Line tools. At the same sime you will need to run a real device or simulator/emulator.  Do not forget to check hostname, port, path and protocol values on your test_settings.json file with your own Appium server.
 
Run the following command in project's base directory :
```
python3 -m pytest examples/local_test/local_android_test.py --alluredir=allure_results
```
 
### All available commands to start mobile testing:
 
 ```
python3 -m pytest examples/getting_started/first_android_test.py --alluredir=allure_results
python3 -m pytest examples/getting_started/first_ios_test.py --alluredir=allure_results
python3 -m pytest examples/local_test/local_android_test.py --alluredir=allure_results
python3 -m pytest examples/local_test/local_ios_test.py --alluredir=allure_results
python3 -m pytest examples/pom_test/tests/pom_android_test.py --alluredir=allure_results
```
 
### Appium Inspector usage with Momentum Suite devices:
 
![image](https://user-images.githubusercontent.com/105457661/173579734-ae2ceae2-70c1-4c00-b58d-cdf81c0b29ef.png)

 
### Allure Reporting
 
 Run the following command in project's base directory after test run has been completed. This command will open a browser window with HTML test results.
```
allure serve allure_results
```

## Getting Help
 
If you are running into any issues or have any queries, please check [Momentum Suite Contact page](https://www.momentumsuite.com/contact/) or get in touch with us.

