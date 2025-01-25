# from selenium import webdriver
from base.webdriver_setup import WebDriverSetup
from pages.login_page import LoginPage
import pytest
import utilities.custom_logger as cl
import logging


@pytest.fixture()
def MethodSetUp():
    log = cl.customLogger(logging.DEBUG)
    # print("\nMethod Set Up - running conftest")
    log.info("Method Set Up - running conftest")
    yield 
    # print("\nMethod Teardown - running conftest")
    log.info("Method Teardown - running conftest")

@pytest.fixture(scope="class")
def ClassSetUp(request, browser):
    log = cl.customLogger(logging.DEBUG)
    # print("\nModule Set Up - running conftest")
    log.info("Module Set Up - running conftest")
    webdriver_instance = WebDriverSetup(browser)
    driver = webdriver_instance.getWebDriverInsance()

    login_page = LoginPage(driver)
    email_login = "test@email.com"
    password_login = "abcabc"
    log.info("Running Default Login")
    login_page.login(email_login, password_login)
    
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    # print("\nModule Teardown - running conftest")
    log.info("Module Teardown - running conftest")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="module")
def browser(request): 
    return request.config.getoption("--browser") 
