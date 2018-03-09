from selenium import webdriver


browser = webdriver.Firefox(executable_path=r'/var/se-drivers/geckodriver')
browser.get('http://mytriorings.com')
print(browser.title)
browser.quit()