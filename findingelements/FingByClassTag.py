from selenium import webdriver


class FindByClassTag:

    def test(self):
        base_url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(base_url)
        print(driver.title)

        elem_by_class_name = driver.find_element_by_class_name('displayed-class')
        elem_by_tag_name = driver.find_element_by_tag_name('h1')

        elem_by_class_name.send_keys('yippee-ki-yay')

        if elem_by_class_name is not None:
            print('Found element by class name')

        if elem_by_tag_name is not None:
            print('Found element by tag name with text: {}'.format(elem_by_tag_name.text))

        driver.quit()


ff = FindByClassTag()
ff.test()
