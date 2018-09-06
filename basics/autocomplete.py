from selenium import webdriver
import time

class AutoComplete:

    def autocomplete(self):

        url = 'https://www.southwest.com/'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)

        driver.find_element_by_id("air-city-departure").send_keys("New")
        time.sleep(3)
        driver.find_element_by_xpath("//ul[@id='air-city-departure-menu']//li[@id='air-city-departure-menu-item3']").\
            click()


obj = AutoComplete()
obj.autocomplete()