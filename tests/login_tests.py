# from selenium import webdriver
# from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import pytest
from utilities.util import Util
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("ClassSetUp", "MethodSetUp")
class LoginTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.login_page_methods = LoginPage(self.driver)
        self.test_results = TestStatus(self.driver)
        self.util = Util()

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.log.info("Running Logout")
        self.login_page_methods.logout()
        self.util.sleep(2, "Wait After Logout")
        
        email = "test@email.com"
        password = "abcabc"
        self.log.info("Running Valid Credentials Login")
        self.login_page_methods.login(email, password)

        self.log.info("Running Title Verified")
        titlePage = self.login_page_methods.verifyLoginTitle()
        self.test_results.mark(titlePage, "Test Title Verified")
        
        self.log.info("Running Verification Login")
        userIcon_locator = "//*[@id='navbar-inverse-collapse']//span[text()='My Account']"
        userIcon = self.login_page_methods.verifyLogin(userIcon_locator)
        self.test_results.markFinal("test_verifyLogin", userIcon, "Login Verified")
    
    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.log.info("Running Logout")
        self.login_page_methods.logout()
        self.util.sleep(2, "Wait After Logout")

        email = "test@email.com"
        password = "abc"
        self.log.info("Running Invalid Credentials Login")
        self.login_page_methods.login(email, password)
        
        self.log.info("Running Invalid Login Message")
        error_locator =  "//span[contains(.,'Incorrect login details')]"
        userIcon = self.login_page_methods.verifyLoginFailed(error_locator)
        assert userIcon == True

        self.util.sleep(2, "Pause Betweem Invalid and Valid test")
