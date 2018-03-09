from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrappers import HandyWrappers


class ElementPresenceCheck:

    def test(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        hw = HandyWrappers(driver)
        driver.get(base_url)
        element_result = hw.elementPresenceCheck("name", By.ID)
        print(element_result)

        driver.quit()


browser = ElementPresenceCheck()
browser.test()
