from base.base_page import BasePage
import utilities.custom_logger as cl
import logging

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    #################################################
    # locators
    #################################################
    my_courses = "MY COURSES"
    all_courses = "ALL COURSES"
    practice = "PRACTICE"
    user_icon = "//img[@class='zl-navbar-rhs-img ']"

    def navigateAllCourses(self):
        self.elementClick(self.all_courses, locatorType="linktext")
    
    def navigateMyCourses(self):
        self.elementClick(self.my_courses, locatorType="linktext")
    
    def navigatePractice(self):
        self.elementClick(self.practice, locatorType="linktext")

    def navigateUserIcon(self):
        self.elementClick(self.user_icon, locatorType="xpath")

    

