from selenium import webdriver


class Test:
    
    def test(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()

        # Window Maximize
        driver.maximize_window()
        # Open the Url
        driver.get(base_url)
        # Get Title
        title = driver.title
        print("Title of the web page is: " + title)
        # Get Current Url
        current_url = driver.current_url
        print("Current Url of the web page is: " + current_url)
        # Browser Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")
        # Open another Url
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?reset_purchase_session=1")
        current_url = driver.current_url
        print("Current Url of the web page is: " + current_url)
        # Browser Back
        driver.back()
        print("Go one step back in browser history")
        current_url = driver.current_url
        print("Current Url of the web page is: " + current_url)
        # Browser Forward
        driver.forward()
        print("Go one step forward in browser history")
        current_url = driver.current_url
        print("Current Url of the web page is: " + current_url)
        # Get Page Source
        page_source = driver.page_source
        #print(page_source)
        # Browser Close / Quit
        driver.close()
        # driver.quit()


obj = Test()
obj.test()
