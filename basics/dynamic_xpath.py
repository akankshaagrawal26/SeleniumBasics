from selenium import webdriver
from selenium.webdriver.common.by import By


class DynamicXpath:

    def dynamic(self):

        driver = webdriver.Firefox()
        driver.maximize_window()
        base_url = "https://learn.letskodeit.com/"
        driver.get(base_url)
        driver.implicitly_wait(10)
        login = driver.find_element(By.LINK_TEXT, "Login").click()
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("abcabc")
        driver.find_element(By.NAME, "commit").click()
        search = driver.find_element(By.ID, "search-courses")
        search.send_keys("JavaScript")
        click_search = driver.find_element(By.ID, "search-course-button")
        click_search.click()
        xpath = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]".format("JavaScript")
        course = driver.find_element(By.XPATH, xpath)
        course.click()


obj = DynamicXpath()
obj.dynamic()