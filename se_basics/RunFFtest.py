from selenium import webdriver


class RunFFTest:

    def test(self):
        driver = webdriver.Firefox(executable_path=r'/var/se-drivers/geckodriver')
        driver.get('http://www.letskodeit.com')
        print(driver.title)
        driver.quit()


ff = RunFFTest()
ff.test()