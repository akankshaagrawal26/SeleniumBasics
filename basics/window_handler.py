from selenium import webdriver
import time


class Handler:
    def handler(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)

        driver.maximize_window()
        driver.get(base_url)

        parentHandler = driver.current_window_handle
        print("parent" + parentHandler)

        driver.find_element_by_id("openwindow").click()
        time.sleep(2)
        all_handlers = driver.window_handles
        print("all_handlers:" + str(all_handlers))

        for handle in all_handlers:
            if handle not in parentHandler:
                print(handle)
                driver.switch_to.window(handle)
                driver.find_element_by_id("search-courses").send_keys("python")
                time.sleep(2)
                driver.close()
                break

        driver.switch_to.window(parentHandler)
        print(driver.current_window_handle)


obj = Handler()
obj.handler()
