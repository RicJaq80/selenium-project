from selenium import webdriver

class WebDriverSetup():

    def __init__(self, browser):
        # we provide the browser, this class will use it and decide
        # which browser is going to use and generate the related driver
        self.browser = browser
    
    def getWebDriverInsance(self):
        # this method will return the instance of the web driver
        # based on the argument that we provide 
        """
        @package based
        WebDriverSetup class implementation
        - it creates a webdriver instance based on the browser configurations
        """
        baseURL = "https://www.letskodeit.com/"
        if self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "edge":
            driver = webdriver.Edge()
        else:
            driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver
