from selenium import webdriver
from selenium.webdriver.common.by import By


class ByDemo:

    def test(self):
        base_url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(base_url)
        print(driver.title)

        elem_by_id = driver.find_element(By.ID, 'name')
        elem_by_xpath = driver.find_element(By.XPATH, '//input[@id="displayed-text"]')
        elem_by_link_text = driver.find_element(By.LINK_TEXT, 'Login')

        if elem_by_id is not None:
            print('Found element by ID')

        if elem_by_xpath is not None:
            print('Found element by Xpath')

        if elem_by_link_text is not None:
            print('Found element by link text')

        driver.quit()

ff = ByDemo()
ff.test()
