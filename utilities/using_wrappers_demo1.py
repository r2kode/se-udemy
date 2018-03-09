from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers
import time


class UsingWrappers:

    def test(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        hw = HandyWrappers(driver)
        driver.get(base_url)

        text_field = hw.getElement("name", "id")
        text_field.send_keys("yippeekiyay")
        time.sleep(3)

        driver.quit()


browser = UsingWrappers()
browser.test()
