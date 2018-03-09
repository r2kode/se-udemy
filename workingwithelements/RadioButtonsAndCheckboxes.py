from selenium import webdriver
import time


class RadioButtonsAndCheckboxes:

    def test(self):
        base_url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)
        print(driver.title)
        bmw_radio_btn = driver.find_element_by_id("bmwradio")
        bmw_radio_btn.click()
        time.sleep(1)
        benz_radio_btn = driver.find_element_by_id("benzradio")
        benz_radio_btn.click()
        time.sleep(1)

        bmw_checkbox = driver.find_element_by_id("bmwcheck")
        bmw_checkbox.click()
        time.sleep(1)
        benz_checkbox = driver.find_element_by_id("benzcheck")
        benz_checkbox.click()
        time.sleep(1)

        print("bmw radio selected? {}".format(bmw_radio_btn.is_selected()))

        driver.quit()


ff = RadioButtonsAndCheckboxes()
ff.test()
