from selenium.webdriver.common.by import By
from pages.register_courses_page import RegisterCourses
from utilities.test_status import TestStatus
import unittest
import pytest
import time
# we need to import these decorators to create a data driven test
from ddt import ddt, data, unpack

# by using data driven testing approach we can use a single test for a set of
# data (or scenarios) by driving the method (in this case: test_invalidEnrollment)
# with various input values 
# we can also separate the test data from the logic, so we can replace the 
# declared variables (ex.: course_name = "javascript") with data from an external
# source like a csv file.
# unitTest has a library called DDT which provides the ability to parametrize
# the test cases 

@pytest.mark.usefixtures("ClassSetUp", "MethodSetUp")
@ddt # add this at the top of the class
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.enrollment_page_methods = RegisterCourses(self.driver)
        self.test_results = TestStatus(self.driver)
    
    
    @pytest.mark.run(order=1)
    # add the data decorator for the method name
    # we add as arguments the number of values that we want to provide
    # 1. in this case we need 4 (num, course_name, exp, cvc)
    # @data(("javascript", "5555 5555 5555 5555", "1225", "555"))
    # 2. now we add another data set
    @data(("JavaScript for beginners", "5555 5555 5555 5555", "1225", "555"), 
          ("Learn Python 3 from scratch", "6666 6666 6666 6666", "1226", "666"))
    # we add four arguments names, pay attention to the order
    # note: if we use lists or tuples we have to use the unpack decorator
    # which unpack them in several arguments
    @unpack
    def test_invalidEnrollment(self, course_name, num, exp, cvc):
        """    
        num = "5555 5555 5555 5555"
        course_name = "javascript"
        exp = "1225"
        cvc = "555"
        """
        self.enrollment_page_methods.enrollCourse(course_name, num, exp, cvc)

        title = "All Courses"
        titlePage = self.enrollment_page_methods.verifyLoginTitle(title)
        self.test_results.mark(titlePage, "Test Title Verified")

        enrollment = self.enrollment_page_methods.verifyEnrollFail()
        self.test_results.markFinal("invalidEnrollment", enrollment, "Enrollment Verified")

        # to go back to All Courses menu
        self.driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        all_courses = "(//a[normalize-space()='ALL COURSES'])[1]"
        self.driver.find_element(By.XPATH, all_courses).click()
