from selenium import webdriver
import time


class HiddenElements:
    def hidden(self):

        url = "https://learn.letskodeit.com/p/practice/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(3)

        element = driver.find_element_by_id("displayed-text")
        state = element.is_displayed()
        print(state)
        time.sleep(2)

        hide = driver.find_element_by_id("hide-textbox").click()
        state = element.is_displayed()
        print(state)
        time.sleep(2)

        show = driver.find_element_by_id("show-textbox").click()
        state = element.is_displayed()
        print(state)


obj = HiddenElements()
obj.hidden()