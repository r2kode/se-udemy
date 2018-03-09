from selenium import webdriver


base_url = "http://dhtmlx.com/docs/products/dhtmlxGrid"
searched_name = "Diana Jakubowski"

driver = webdriver.Firefox()
driver.get(base_url)
print(driver.title)
search_field = driver.find_element_by_xpath("//div[starts-with(@id, 'cgrid2_')]//table//tr[3]/td[2]//input[@type='text']")
# search_field = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[1]/table/tbody/tr[3]/td[2]/div/input")
search_field.send_keys(searched_name)
result_xpath = "//div[contains(@class,'objbox')]/table/tbody/tr[2]/td[@title='{}']//following-sibling::td".format(searched_name)
search_result = driver.find_element_by_xpath(result_xpath).text
print(search_result)

driver.quit()
