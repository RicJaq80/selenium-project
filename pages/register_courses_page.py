from base.base_page import BasePage
import utilities.custom_logger as cl
import logging
import time

class RegisterCourses(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    #################################################
    # locators
    #################################################
    all_courses = "(//a[normalize-space()='ALL COURSES'])[1]"
    search_box = "course" # name - send keys
    search_button = "//button[@class='find-course search-course']" # xpath - click
    # course = "//h4[normalize-space()='JavaScript for beginners']" # xpath - click
    # course = "(//h4[normalize-space()])[1]"
    # for course locator:
    course = "//h4[normalize-space()='{0}']"
    enroll_button = "//button[normalize-space()='Enroll in Course']" # xpath - click
    # cc_num = "cardnumber" # name - send keys
    cc_num = "//input[@aria-label='Credit or debit card number']" # xpath - send keys
    cc_exp = "exp-date" # name - send keys
    cc_cvc = "cvc" # name - send keys
    # submit_enroll = ""
    enroll_err_msg = "(//span[normalize-space()='Your card number is invalid.'])[1]"
    # //div/ul/li[contains(.,'Your card number is invalid.')]
    
    ##################################################
    # actions
    ##################################################
    # to display all courses
    # all_courses = "//a[text()='ALL COURSES']"//a[text()='ALL COURSES']"
    def clickAllCourses(self):
        self.elementClick(self.all_courses, locatorType="xpath")
    

    # to introduce the selected course
    # search_box = "course"
    def enterCourseName(self, courseName):
        self.elementSendKeys(courseName, self.search_box, locatorType="name")
    
    
    # click on the search button
    # search_button = "//button[@class='find-course search-course']"
    def clickSearchButton(self):
        self.elementClick(self.search_button, locatorType="xpath")
    

    # click on the searched course
    # //h4[normalize-space()='JavaScript for beginners']
    # or
    # course = "//h4[normalize-space()='{}']"
    def clickSelectCourse(self, course):
    # def clickSelectCourse(self):
        # self.elementClick(self.course, locatorType="xpath")
        self.elementClick(self.course.format(course), locatorType="xpath")
    
    
    # click on the Enroll in Course button
    # enroll_button = "//button[normalize-space()='Enroll in Course']"
    def clickEnrollCourse(self):
        self.elementClick(self.enroll_button, locatorType="xpath")
    

    # to introduce invalid credit card number
    # cc_num = "card-number"
    def enterCardNum(self, num):
        # iFrame name is dynamic
        self.log.info("Enter Credit Card Number")
        time.sleep(2)
        # self.switchToFrame(name="__privateStripeFrame0543")
        # self.switchToFrame(index=2)
        self.switchFrameByIndex(self.cc_num, locatorType="xpath")
        # self.elementSendKeys(num, self.cc_num, locatorType="name")
        self.sendKeysWhenReady(num, self.cc_num, locatorType="xpath")
        self.switchDefaultContent()
    
    # to introduce invalid credit card number
    # cc_cvc = "cvc"
    def enterCardCvc(self, cvc):
        # iFrame name is dynamic
        # self.switchToFrame(name="__privateStripeFrame0544")
        self.log.info("Enter Credit Card CVV")
        time.sleep(2)
        self.switchFrameByIndex(self.cc_cvc, locatorType="name")
        self.elementSendKeys(cvc, self.cc_cvc, locatorType="name")
        self.switchDefaultContent()
    
    # to introduce invalid credit card number
    # cc_exp = "exp-date"
    def enterCardDate(self, exp):
        # iFrame name is dynamic
        # self.switchToFrame(name="__privateStripeFrame0545")
        self.log.info("Enter Credit Card Expiration Date")
        time.sleep(2)
        self.switchFrameByIndex(self.cc_exp, locatorType="name")
        self.elementSendKeys(exp, self.cc_exp, locatorType="name")
        self.switchDefaultContent()
    
    def enterCardInformation(self, num, exp, cvc):
        self.enterCardNum(num)
        self.enterCardCvc(cvc)
        self.enterCardDate(exp)


    def enrollCourse(self, course_name, num="", exp="", cvc=""):
        """
        - click on the enroll button
        - scroll down
        - enter card information
        - click on the enroll in course button
        """
        time.sleep(2)
        self.clickAllCourses()
        self.enterCourseName(course_name)
        time.sleep(2)
        self.clickSearchButton()
        time.sleep(2)
        # self.clickSelectCourse()
        self.clickSelectCourse(course_name)
        self.clickEnrollCourse()
        self.scrollBrowser(direction="down")
        self.enterCardInformation(num, exp, cvc)
    

    # verify the error message
    # enroll_err_msg = "(//span[normalize-space()='Your card number is invalid.'])[1]"
    def verifyEnrollFail(self):
        """
        - verify the element of the error message is displayed - not only present
        """
        err_msg = self.isElementDisplayed(self.enroll_err_msg, locatorType="xpath")
        return err_msg
    

    def verifyLoginTitle(self, title):
        return self.verifyPageTitle(title)
