from selenium import webdriver
import time


class Scrolling:

    def scroll(self):

        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)

        driver.maximize_window()
        driver.get(base_url)
        driver.execute_script("window.scrollBy(0,2000);")  #scroll down
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-2000);")
        time.sleep(3)
        el = driver.find_element_by_id("mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", el)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-150);")
        driver.execute_script("window.scrollBy(0,-2000);")
        loc = el.location_once_scrolled_into_view
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-150);")

        print(driver.get_window_size())


obj = Scrolling()
obj.scroll()