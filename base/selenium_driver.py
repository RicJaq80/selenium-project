from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
import utilities.custom_logger as cl
import logging

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
    

    def getTitle(self):
        return self.driver.title


    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info(locatorType + ". Locator type is not supported/correct")
        return False


    def getElement(self, locator, locatorType = "id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element: " + str(locator) + " is found")
        except:
            self.log.error("Element: " + str(locator) + " is not found")
        return element


    def getElements(self, locator, locatorType = "id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Elements: " + str(locator) + " are found")
        except:
            self.log.error("Elements: " + str(locator) + " are not found")
        return element
    
    def getElementText(self, locator, locatorType = "id", element=None):
        element = None
        try:
            if locator:
                byType = self.getByType(locatorType)
                element = self.driver.find_element(byType, locator)
            txt = element.text
            if len(txt) == 0:
                txt = element.get_attribute("innerText")
            else:
                self.log.info("Element: " + str(locator) + "hast text: " + txt)
                txt = txt.strip()
        except:
            self.log.error("Element: " + str(locator) + "has no text")
        return txt
        

    def elementClick(self, locator, locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Element: " + str(locator) + " is clickable")
        except:
            self.log.error("Element: " + str(locator) + " is not clickable")
            print_stack()
    

    def elementSendKeys(self, text, locator, locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(text)
            self.log.info("Element: " + str(locator) + " received text: " + text)
        except:
            self.log.error("Element: " + str(locator) + " did not receive text: " + text)
            # print_stack()
    

    def sendKeysWhenReady(self, data, locator="", locatorType="id"):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(10) +
                          " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=10,
                                 poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            self.log.info("Element appeared on the web page")
            element.click()
            element.send_keys(data)

            if element.get_attribute("value") != data:
                self.log.debug("Text is not sent by xpath in field, send string char by char!")
                element.clear()
                for i in range(len(data)):
                    element.send_keys(data[i] + "")
            self.log.info("Sent data on element with locator: " + locator)
        except:
            self.log.info("Element: " + locator + " not found")


    def isElementPresent(self, locator, locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element: " + str(locator) + " is present")
                return True
            else:
                self.log.error("Element: " + str(locator) + " is not present")
                return False
        except:
            # print("Element or Locator not correct")
            self.log.error("Element or Locator not correct - not found")
            return False


    def isElementListPresent(self, locator, locatorType="id"):
        try:
            elementList = self.getElements(locator, locatorType)
            if len(elementList) > 0:
                self.log.info("Element List is found")
                return True
            else:
                self.log.warning("Element List not found")
                return False
        except:
            self.log.error("Element List or Locator not correct - not found")
            return False


    def isElementDisplayed(self, locator, locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element: " + str(locator) + " is displayed")
            else:
                self.log.error("Element: " + str(locator) + " is not displayed")
            return isDisplayed
        except:
            # print("Element or Locator not correct")
            self.log.error("Element or Locator not correct - not found")
            return False
    

    def waitForElement(self, locator, locatorType = 'id', timeout_1 = 10, 
                       pollFrequency = 0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum: " + str(timeout_1) + 
                  ": seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout_1, poll_frequency=pollFrequency, 
                                 ignored_exceptions=[NoSuchElementException, 
                                                     ElementNotVisibleException, 
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            self.log.info("Element: " + str(locator) + " appeared on the web page")
        except:
            self.log.error("Element: " + str(locator) + " DID NOT appear on the web page")
            # print_stack()
        return element
    

    def scrollBrowser(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -800);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0,800)")
        else:
            self.log.error("Wrong Direction Request")

    
    def switchToFrame(self, id="", name="", index=None):
        """
        Switch to iFrame using element locator inside iFrame

        Parameters:
            1. Required: None
            2. Optional:
                - id: id of the iframe
                - name: name of the iframe
                - index: index of the iframe
        """
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)
    

    def switchDefaultContent(self):
        self.driver.switch_to.default_content()
    

    def switchFrameByIndex(self, locator, locatorType="xpath"):
        """
        Get the iFrame using the element locator inside the iFrame

        Parameters:
            1. Required:
                - locator: locator of the element
            2. Optional:
                - locatorType: locator type to find the element
        """
        result = False
        try:
            # //iframe is the locator to all the iframes on the DOM
            iframe_list = self.getElements("//iframe", locatorType="xpath")
            self.log.info("Length of iframe: " + str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.log.info("iFrame index: " + str(i))
                self.switchToFrame(index=iframe_list[i])
                result = self.isElementPresent(locator, locatorType)
                if result:
                    self.log.info("iFrame index found is: " + str(i))
                    break
                # if the i iFrame is not the expected one, we return to the
                # default content and then try the next i iFrame
                self.switchDefaultContent()
            return result
        except:
            self.log.error("iFrame index not found")
            return result


    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute element

        Parameters:
            1. Required:
                - attribute: attribute whose value to find
            2. Optional:
                - element: element whose attribute we need to find
                - locator: locator of the element
                - locatorType: locator type to find the element
        Returns:
            Value of the attribute
        """
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value
    

    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                - locator: locator of the element to check
            2. Optional:
                - locatorType: type of the locator
                - info: information about the element, label/name of the element
        """
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element,
                                                           attribute="disabled")
            if attributeValue is not None:
                enabled = enabled.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element,
                                                      attribute="class")
                self.log.info("Attribute value from applicatoin web UI: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element: " + info + " is enabled")
            else:
                self.log.info("Element: " + info + " is not enabled")
        except:
            self.log.error("Element: " + info + " state could not be found")
        return enabled
