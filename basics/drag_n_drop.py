from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class DragDrop:

    def drag_drop(self):

        url = "https://jqueryui.com/droppable/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        driver.switch_to.frame(0)
        drag = driver.find_element_by_id("draggable")
        drop = driver.find_element_by_id("droppable")

        try:
            actions = ActionChains(driver)
            # actions.drag_and_drop(drag,drop).perform()
            actions.click_and_hold(drag).move_to_element(drop).release().perform()
            time.sleep(2)
            print("drag and dropped")

        except:
            print("Drag and drop failed")


obj = DragDrop()
obj.drag_drop()