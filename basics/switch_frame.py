from selenium import webdriver
import time


class SwitchFrame:

    def frame_switch(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)

        driver.maximize_window()
        driver.get(base_url)

        driver.switch_to.frame("courses-iframe")    #id
        # driver.switch_to.frame("iframe-name")     #name
        # driver.switch_to.frame(0)                 #number
        time.sleep(2)
        driver.find_element_by_id("search-courses").send_keys("python")

        time.sleep(2)
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,2000);")
        time.sleep(2)
        driver.find_element_by_id("name").send_keys("abc")
        driver.quit()
        

obj = SwitchFrame()
obj.frame_switch()
