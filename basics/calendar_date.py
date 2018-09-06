from selenium import webdriver
from selenium.webdriver.common.by import By


class CalendarDate:

    def calendardate(self):

        url = 'http://www.expedia.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()

        driver.find_element(By.ID, "flight-departing-hp-flight").click()
        cal_month = driver.find_element(By.XPATH,"//div[@class='datepicker-cal-month']//button[@data-day='30']")
        cal_month.click()


obj = CalendarDate()
obj.calendardate()