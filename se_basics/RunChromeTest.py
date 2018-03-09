from selenium import webdriver
import os


class RunChromeTest:

    def test(self):
        driver_location = '/var/se-drivers/chromedriver'
        # os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get('http://www.letskodeit.com')
        print(driver.title)
        driver.quit()


chrome = RunChromeTest()
chrome.test()
