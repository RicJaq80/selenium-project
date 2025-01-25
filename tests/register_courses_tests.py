from pages.register_courses_page import RegisterCourses
from utilities.test_status import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("ClassSetUp", "MethodSetUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.enrollment_page_methods = RegisterCourses(self.driver)
        self.test_results = TestStatus(self.driver)
    
    
    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        num = "5555 5555 5555 5555"
        course_name = "javascript"
        exp = "1225"
        cvc = "555"
        # modify the enrollCourse method to only access to All Courses
        self.enrollment_page_methods.enrollCourse(course_name, num, exp, cvc)
        # create method to display all courses and then:
        title = "All Courses"
        titlePage = self.enrollment_page_methods.verifyLoginTitle(title)
        self.test_results.mark(titlePage, "Test Title Verified")


        enrollment = self.enrollment_page_methods.verifyEnrollFail()
        self.test_results.markFinal("invalidEnrollment", enrollment, "Enrollment Verified")
