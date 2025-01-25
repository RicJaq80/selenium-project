import unittest
from tests.login_tests import LoginTests
from tests.register_courses_csv_data import RegisterTests

# get all the tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterTests)

# create a test suite combining all test cases
regressionTest = unittest.TestSuite([tc1, tc2])

# execute test suite
unittest.TextTestRunner(verbosity=2).run(regressionTest)
