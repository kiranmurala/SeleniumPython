from selenium import webdriver
import os

class RunIETests():

    def ie_tests(self):
        driver_location = "D:\\SeleniumPython\\lib\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = driver_location
        driver = webdriver.Ie(driver_location)
        driver.get("http://www.letskodeit.com")

ie_test = RunIETests()
ie_test.ie_tests()