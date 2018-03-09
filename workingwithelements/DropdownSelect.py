from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class DropdownSelect:

    def test(self):
        base_url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)
        print(driver.title)

        dropdown = driver.find_element_by_id("carselect")
        sel = Select(dropdown)

        print("select benz by value")
        sel.select_by_value("benz")
        time.sleep(1)

        print("select honda by index")
        sel.select_by_index(2)
        time.sleep(1)

        print("select bmw by visible text")
        sel.select_by_visible_text("BMW")
        time.sleep(1)

        print("select honda by index")
        sel.select_by_index("2")
        time.sleep(1)

        driver.quit()


ff = DropdownSelect()
ff.test()
