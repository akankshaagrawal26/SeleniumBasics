from selenium import webdriver


class RunFirefox:

    def test(self):

        driver = webdriver.Firefox()
        driver.get("http://www.google.com")


run = RunFirefox()
run.test()
