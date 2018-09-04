from selenium import webdriver
import os


class RunChrome:

    def test(self):

        driver_location = "D:\\Selenium\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("http://www.google.com")


run = RunChrome()
run.test()
