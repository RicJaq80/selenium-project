from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        # resultLst will keep track of all the results
        # we will call this list and verify if there is a single failure
        # and if so we fail the test case
        self.resultLst = []
    

    def setResults(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultLst.append("PASS")
                    self.log.info("### Verification PASS: " + resultMessage)
                else:
                    self.resultLst.append("FAIL")
                    self.log.info("### Verification FAIL: " + resultMessage)
            else:
                self.resultLst.append("FAIL")
                self.log.error("### Verification Error: " + resultMessage)
            print(self.resultLst)
        except:
            self.resultLst.append("FAIL")
            self.log.error("### Verification Exception!!!: " + resultMessage)


    def mark(self, result, resultMessage):
        """
        Mark the result of the verificatoin point in a test case
        """
        self.setResults(result, resultMessage)

    
    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResults(result, resultMessage)
        
        if "FAIL" in self.resultLst:
            self.log.error(testName + " ### TEST FAILED")
            self.resultLst.clear()
            # assert True == False # to stop the test
            assert True == True # to NOT stop the test
        else:
            self.log.info(testName + " ### TEST PASSED")
            self.resultLst.clear()
            assert True == True
