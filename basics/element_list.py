from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ElementList:
    def element_list(self):
        url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)

        checkboxes_list = driver.find_elements(By.XPATH, "//input[contains(@name,'cars') and contains(@type,"
                                                         "'checkbox')]")
        size = len(checkboxes_list)
        print(size)
        for checkboxes in checkboxes_list:
            if_select = checkboxes.is_selected()
            if not if_select:
                checkboxes.click()
                time.sleep(2)


obj = ElementList()
obj.element_list()
