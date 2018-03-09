from selenium import webdriver
from selenium.webdriver.common.by import By
from wait_types.explicit_wait_type import ExplictWaitType
import time


class ExplicitWaitDemo:

    def test(self):
        base_url = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        wait = ExplictWaitType(driver)
        driver.get(base_url)
        print(driver.title)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("YTO")
        driver.find_element(By.ID, "flight-departing-hp-flight").click()
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("2/27/2018")
        return_date = driver.find_element(By.ID, "flight-returning-hp-flight")
        return_date.clear()
        return_date.send_keys("2/03/2018")
        driver.find_element(By.XPATH, "//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']").click()
        # driver.find_element(By.ID, "stopFilter_stops-0").click() # need to use explicit wait

        element = wait.waitForElement("stopFilter_stops-0", "id", 20)
        element.click()

        time.sleep(5)
        driver.quit()


browser = ExplicitWaitDemo()
browser.test()

