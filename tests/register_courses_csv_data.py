# from selenium.webdriver.common.by import By
from pages.register_courses_page import RegisterCourses
from pages.navigation_page import NavigationPage
from utilities.test_status import TestStatus
from utilities.read_data import getCsvData
import unittest
import pytest
import time
# we need to import these decorators to create a data driven test
from ddt import ddt, data, unpack
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("ClassSetUp", "MethodSetUp")
@ddt # add this at the top of the class
class RegisterTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.enrollment_page_methods = RegisterCourses(self.driver)
        self.test_results = TestStatus(self.driver)
        self.navigation = NavigationPage(self.driver)
    
    
    # @data(("JavaScript for beginners", "5555 5555 5555 5555", "1225", "555"), 
    #      ("Learn Python 3 from scratch", "6666 6666 6666 6666", "1226", "666"))
    # we pass in the getCsvData method
    # we use * to indicate python that there will be several arguments
    # the path argument will be unpacked in a list
    @data(*getCsvData("C:/RespaldoCursos/SeleniunWebDriver/LetsKodeIt/Automation/Framework/3.Project_CSV/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, course_name, num, exp, cvc):
        """    
        num = "5555 5555 5555 5555"
        course_name = "javascript"
        exp = "1225"
        cvc = "555"
        """
        self.log.info("Running Enroll Course")
        self.enrollment_page_methods.enrollCourse(course_name, num, exp, cvc)

        # title = "All Courses"
        self.log.info("Running Title Verified")
        titlePage = self.enrollment_page_methods.verifyLoginTitle(course_name)
        self.test_results.mark(titlePage, "Test Title Verified")

        self.log.info("Running Invalid Enrollment")
        enrollment = self.enrollment_page_methods.verifyEnrollFail()
        self.test_results.markFinal("invalidEnrollment", enrollment, "Enrollment Verified")

        self.log.info("Scroll Up")
        self.driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        # we comment some of these lines to use the NavigationPage class
        # all_courses = "(//a[normalize-space()='ALL COURSES'])[1]"
        # self.driver.find_element(By.XPATH, all_courses).click()
        self.log.info("Running navigate to All Courses")
        self.navigation.navigateAllCourses()
