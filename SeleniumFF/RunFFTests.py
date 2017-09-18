from selenium import webdriver

class RunFFTests():

    def test(self):
        driver = webdriver.Firefox()
        driver.get("http://www.letskodeit.com")


ff = RunFFTests()
ff.test()