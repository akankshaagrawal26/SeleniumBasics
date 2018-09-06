from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshot:

    def test(self):

        base_url = "https://learn.letskodeit.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)

        driver.maximize_window()
        driver.get(base_url)
        login_link = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        login_link.click()
        time.sleep(5)
        driver.find_element(By.ID, "user_email").send_keys("akki@gmail.com")
        driver.find_element(By.ID, "user_password").send_keys("password")
        driver.find_element_by_name("commit").click()

        screenshotPath = "D://test.png"
        try:
            driver.save_screenshot(screenshotPath)
            print("screenshot taken")
        except NotADirectoryError:
            print("exception")


obj = Screenshot()
obj.test()