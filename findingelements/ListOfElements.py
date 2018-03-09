from selenium import webdriver


class ListOfElements:

    def test(self):
        base_url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(base_url)
        print(driver.title)

        class_name = "inputs"
        tag_name = "a"
        elem_list_by_class_name = driver.find_elements_by_class_name(class_name)
        elem_list_by_tag_name = driver.find_elements_by_tag_name(tag_name)

        if elem_list_by_class_name is not None:
            print('There is {1} elements with class name "{0}" on page'.format(class_name, len(elem_list_by_class_name)))

        if elem_list_by_tag_name is not None:
            print('Found {1} "{0}" tag elements on page'.format(tag_name, len(elem_list_by_tag_name)))

        driver.quit()


ff = ListOfElements()
ff.test()