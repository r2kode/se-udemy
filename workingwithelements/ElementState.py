from selenium import webdriver


class ElementState:

    def is_enabled(self):
        base_url = 'http://google.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)
        print(driver.title)

        e1 = driver.find_element_by_id("gs_htif0")
        e1_state = e1.is_enabled()
        print(e1_state)

        e2 = driver.find_element_by_id("gs_taif0")
        e2_state = e2.is_enabled()
        print(e2_state)

        e3 = driver.find_element_by_id("lst-ib")
        e3_state = e3.is_enabled()
        print(e3_state)

        e3.send_keys("letskodeit")

        driver.quit()


ff = ElementState()
ff.is_enabled()
