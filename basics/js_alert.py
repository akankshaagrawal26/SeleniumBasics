from selenium import webdriver
import time


class JsAlert:

    def js_alert(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)

        driver.maximize_window()
        driver.get(base_url)

        driver.find_element_by_id("name").send_keys("abc")
        driver.find_element_by_id("alertbtn").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.find_element_by_id("name").send_keys("abc")
        driver.find_element_by_id("confirmbtn").click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()


obj = JsAlert()
obj.js_alert()