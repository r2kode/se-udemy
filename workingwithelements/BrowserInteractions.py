from selenium import webdriver


class BrowserInteractions:

    def test(self):
        base_url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        print(driver.title)
        print(driver.current_url)
        driver.get(driver.current_url)
        driver.refresh()
        driver.get('https://mytriorings.com')
        driver.back()
        driver.forward()
        print(driver.page_source)

        driver.quit()


ff = BrowserInteractions()
ff.test()