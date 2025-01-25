# from selenium.webdriver.common.by import By
# from base.selenium_driver import SeleniumDriver
from base.base_page import BasePage
from pages.navigation_page import NavigationPage
import utilities.custom_logger as cl
import logging

# all page classes shall inherit from base page class
# base page class already inherits from SeleniumDriver class
# class LoginPage(SeleniumDriver):
class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver # test runs normally if this line is commented
        self.navigation = NavigationPage(driver)

    #################################################
    # locators
    #################################################
    login_link = "dynamic-link[href='/login']"
    email_field = "email"
    password_field = "login-password"
    login_button = "login"

    ##################################################
    # actions
    ##################################################
    def clickLoginLink(self):
        self.elementClick(self.login_link, locatorType="classname")
    
    def enterEmail(self, email):
        self.elementSendKeys(email, self.email_field)
    
    def enterPassword(self, password):
        self.elementSendKeys(password, self.password_field)
    
    def clickLoginButton(self):
        self.elementClick(self.login_button)
    
    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
 
    def verifyLogin(self, locator):
        userIcon = self.isElementPresent(locator, locatorType="xpath")
        return userIcon
    
    def verifyLoginFailed(self, locator):
        result = self.isElementPresent(locator, locatorType="xpath")
        return result
    
    def clearFields(self):
        emailField = self.getElement(locator=self.email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self.password_field)
        passwordField.clear()

    # this code is moved and modified on base_page.py since it can be used for
    # different tests
    def verifyLoginTitle(self):
        """
            if "Login" in self.getTitle():
                return True
            else:
                return False
        """
        title = "Login"
        return self.verifyPageTitle(title)

    # method to logout
    def logout(self):
        self.navigation.navigateUserIcon()
        self.elementClick(locator="//a[@href='/logout']", locatorType="xpath")
    
