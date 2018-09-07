from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class MouseHover:

    def hover(self):

        url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)

        driver.execute_script("window.scrollBy(0, 600);")
        element = driver.find_element_by_id("mousehover")
        top_link = driver.find_element(By.XPATH,"//div[@class='mouse-hover-content']//a[@href='#top']")
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            time.sleep(2)
            actions.move_to_element(top_link).click().perform()
            # top_link.click()
            print("mouse clicked")

        except:
            print("Mouse hover failed")


obj = MouseHover()
obj.hover()