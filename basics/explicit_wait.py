from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
import time
import os


class ExplicitWait:

    def explicit(self):
        driver_location = "D:\\Selenium\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driver_location
        driver = webdriver.Chrome(driver_location)

        base_url = "http://www.expedia.com"
        # driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("09/07/2018")
        ret = driver.find_element(By.ID, "flight-returning-hp-flight")
        ret.clear()
        ret.send_keys("09/08/2018")
        driver.find_element(By.XPATH, "//form[@id='gcw-flights-form-hp-flight']//label/button").click()

        wait = WebDriverWait(driver, 15, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
        element = wait.until(ec.element_to_be_clickable((By.ID, "stopFilter_stops - 0")))
        element.click()

        time.sleep(2)
        driver.quit()


obj = ExplicitWait()
obj.explicit()
