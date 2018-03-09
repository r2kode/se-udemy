from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WorkingWithElementsList:

    def test(self):
        base_url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)
        print(driver.title)

        radio_button_list = driver.find_elements(By.XPATH, "//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        size = len(radio_button_list)
        print("size of list {}".format(size))

        for radio_btn in radio_button_list:
            if not radio_btn.is_selected():
                radio_btn.click()
            time.sleep(1)

        driver.quit()


ff = WorkingWithElementsList()
ff.test()
