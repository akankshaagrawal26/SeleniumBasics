from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ElementState:

    def state(self):

        driver = webdriver.Firefox()
        driver.maximize_window()
        base_url = "http://www.google.com"
        driver.get(base_url)
        driver.implicitly_wait(10)
        id1 = driver.find_element(By.ID, "lst-ib")
        if id1.is_enabled():
            id1.send_keys("github")
        else:
            print("Its disabled")

        url = "https://learn.letskodeit.com/p/practice"
        driver.get(url)
        bmw = driver.find_element(By.ID, "bmwradio")
        bmw.click()
        time.sleep(3)
        honda = driver.find_element(By.ID, "hondaradio")
        honda.click()
        res = honda.is_selected()
        print(res)


obj = ElementState()
obj.state()
