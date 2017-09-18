from selenium import webdriver
import os

class RunChromeTests():

    def chrome_tests(self):
        driver_location = "D:\\SeleniumPython\\lib\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("http://www.letskodeit.com")

chromeTest = RunChromeTests()
chromeTest.chrome_tests()
