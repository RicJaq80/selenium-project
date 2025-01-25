import time
import traceback
# import random, string
import utilities.custom_logger as cl
import logging


class Util():

    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, reason= ""):
        """
        Put the program to wait and give a reason why
        """
        try:
            self.log.info("Wait: " + str(sec) + " seconds due to: " + reason)
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()


    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string
        Parameter:
            - expectedLst
            - actualLst
        """
        self.log.info("Received Title Text: " + actualText)
        self.log.info("Expected Title Text: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### Title Verification PASS")
            return True
        else:
            self.log.info("### Title Verification FAIL")
            return False 
    
    
    def verifyTextMatches(self, actualText, expectedText):
        """
        Verify actual text contains expected text string
        Parameter:
            - expectedLst
            - actualLst
        """
        self.log.info("Received Title Text: " + actualText)
        self.log.info("Expected Title Text: " + expectedText)
        if expectedText.lower() == actualText.lower():
            self.log.info("### Title Verification PASS")
            return True
        else:
            self.log.info("### Title Verification FAIL")
            return False
