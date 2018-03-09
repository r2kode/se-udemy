from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys:

    def test(self):
        base_url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)
        print(driver.title)
        driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']").click()
        email_field = driver.find_element(By.ID, "user_email")
        email_field.send_keys("test")
        pswd_field = driver.find_element(By.ID, "user_password")
        pswd_field.send_keys("password")
        email_field.clear()
        time.sleep(3)
        email_field.send_keys("another user")

        driver.quit()


ff = ClickAndSendKeys()
ff.test()