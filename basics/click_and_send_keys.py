from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:

    def test(self):

        base_url = "https://learn.letskodeit.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)

        driver.maximize_window()
        driver.get(base_url)
        login_link = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        login_link.click()

        email = driver.find_element(By.ID, "user_email")
        email.send_keys("akki@gmail.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("password")

        email.clear()
        email.send_keys("test")


obj = Test()
obj.test()




