from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Screenshot:

    def test(self):
        base_url = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)
        print(driver.title)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()

        self.take_screenshot(driver)

        driver.quit()

    def take_screenshot(self, driver):
        file_name = str(round(time.time() * 100)) + ".png"
        screenshot_dir = "/home/artur/selenium/udemy/utilities"
        file_path = screenshot_dir + file_name

        try:
            driver.save_screenshot(file_path)
            print("Screenshot saved in {}".format(file_path))
        except NotADirectoryError:
            print("failed to save screenshot")


browser = Screenshot()
browser.test()