from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class DropdownElement:

    def dropdown(self):
        url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)

        element = driver.find_element_by_id("carselect")
        sel = Select(element)

        sel.select_by_index(2)     # or  sel.select_by_index("2")
        time.sleep(5)
        sel.select_by_value("bmw")
        time.sleep(5)
        sel.select_by_visible_text("Benz")


obj = DropdownElement()
obj.dropdown()
