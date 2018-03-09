from selenium import webdriver


base_url = 'https://letskodeit.teachable.com/pages/practice'
driver = webdriver.Firefox()
driver.get(base_url)
print(driver.title)
book_title = driver.find_element_by_xpath("//table[@id='product']//tr[3]/td[2]")
print(book_title.text)
driver.quit()
