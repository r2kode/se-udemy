from selenium import webdriver


class FindByLinkText:

    def test(self):
        base_url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(base_url)
        print(driver.title)

        elem_by_link_text = driver.find_element_by_link_text('Practice')
        elem_by_partial_link_text = driver.find_element_by_partial_link_text('Logi')

        if elem_by_link_text is not None:
            print('element by link text found')

        if elem_by_partial_link_text is not None:
            print('element by partial link text found')

        driver.quit()


ff = FindByLinkText()
ff.test()
