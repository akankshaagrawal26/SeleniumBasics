from selenium import webdriver
import os


class RunIE:

    def test(self):

        driver_location = "D:\\Selenium\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = driver_location
        driver = webdriver.Ie(driver_location)
        driver.get("http://www.google.com")


run = RunIE()
run.test()