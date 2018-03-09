from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class FindByXpathCss:

    def test(self):
        base_url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(base_url)
        print(driver.title)
        elem_by_xpath = driver.find_element_by_xpath("//input[@id='name']")
        elem_by_css = driver.find_element_by_css_selector('#displayed-text')

        if elem_by_xpath is not None:
            print('element by xpath found')

        if elem_by_css is not None:
            print('element by css found')

        driver.quit()


ff = FindByXpathCss()
ff.test()
