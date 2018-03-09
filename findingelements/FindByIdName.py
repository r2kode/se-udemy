from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class FindByIdName:

    def test(self):
        base_url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(base_url)
        print(driver.title)
        elem_by_id = driver.find_element_by_id('name')
        elem_by_name = driver.find_element_by_name('show-hide')

        if elem_by_id is not None:
            print('element by id found')

        if elem_by_name is not None:
            print('element by name found')

        driver.get('https://yahoo.com')
        try:
            yui_elem = driver.find_element_by_id('yui_3_18_0_4_1518643831465_1125')
            print(yui_elem)
        except NoSuchElementException:
            print('zdupcyło się')

        driver.quit()


ff = FindByIdName()
ff.test()
