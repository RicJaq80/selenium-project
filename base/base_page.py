# actions/methods common to all the pages
from base.selenium_driver import SeleniumDriver
from utilities.util import Util

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver # tests run normally if this line is commented
        self.util = Util() # instance of the Util class}
    
    
    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page title
        Parameters: title_to_verify
        - title on the page that needs to be verified
        """
        try:
            receivedTitle = self.getTitle() # title received from the browser
            return self.util.verifyTextContains(receivedTitle, titleToVerify)
        except:
            self.log.error("Failed to get the page Title")
            return False
