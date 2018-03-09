from selenium.webdriver.common.by import By


class HandyWrappers:

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class_name":
            return By.CLASS_NAME
        elif locator_type == "link_text":
            return By.LINK_TEXT
        else:
            print("locator type not supported")
            return False

    def getElement(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.getByType(locator_type)
            element = self.driver.find_element(by_type, locator)
            print("element found")
        except:
            print("element not found")
        return element

    def isElementPresent(self, locator, byType):
        element = None
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                return True
            else:
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementsList = self.driver.find_elements(byType, locator)
            if len(elementsList) > 0:
                return True
            else:
                return False
        except:
            print("element not found")
            return False

