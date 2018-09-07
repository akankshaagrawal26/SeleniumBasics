from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class Sliding:

    def slide(self):

        url = "https://jqueryui.com/slider/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        driver.switch_to.frame(0)
        element_to_slide = driver.find_element_by_xpath("//div[@id='slider']//span")
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element_to_slide, 200, 0).perform()
            time.sleep(2)
            print("element slided")

        except:
            print("sliding failed")


obj = Sliding()
obj.slide()