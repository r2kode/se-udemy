from selenium import webdriver
import time


class DynamicXPath:

    def test(self):
        base_url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)
        print(driver.title)

        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("user_email").send_keys("test@email.com")
        driver.find_element_by_id("user_password").send_keys("abcabc")
        driver.find_element_by_name("commit").click()

        search_phrase = "JavaScript"
        driver.find_element_by_id("search-courses").send_keys(search_phrase)
        driver.find_element_by_id("search-course-button").click()

        _course = "//div[contains(@class, 'course-listing-title') and contains(text(), '{}')]".format(search_phrase)
        driver.find_element_by_xpath(_course).click()
        time.sleep(3)
        print(driver.title)

        driver.quit()


browser = DynamicXPath()
browser.test()