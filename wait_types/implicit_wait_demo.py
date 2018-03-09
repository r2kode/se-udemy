from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ImplicitWaitDemo:

    def test(self):
        base_url = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        print(driver.title)
        driver.implicitly_wait(3)

        login_link = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        login_link.click()

        email_field = driver.find_element(By.ID, "user_email")
        email_field.send_keys("test")

        time.sleep(3)
        driver.quit()


browser = ImplicitWaitDemo()
browser.test()
