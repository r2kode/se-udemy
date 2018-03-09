from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class Airbnb:

    def test(self):
        base_url = "https://www.airbnb.com/a/"
        driver = webdriver.Firefox()
        
        driver.maximize_window()
        driver.get(base_url)
        print(driver.title)
        time.sleep(2)

        where = "Toronto"
        check_in = ""
        check_out = ""
        adults = "4"
        children = "2"

        where_input = "lp-geocomplete"
        checkin_input = ""
        checkout_input = ""

        driver.find_element_by_id("lp-geocomplete").send_keys(where)
        driver.find_element_by_id("checkin_input").click()
        driver.find_element_by_id("checkout_input").click()
        adult_select = Select(driver.find_element_by_id("adults"))
        adult_select.select_by_value(adults)
        children_select = Select(driver.find_element_by_id("children"))
        children_select.select_by_value(children)

        driver.find_element_by_xpath("//div[@id='lp-search-button']/button").click()

        print(driver.title)

        driver.quit()


browser = Airbnb()
browser.test()
