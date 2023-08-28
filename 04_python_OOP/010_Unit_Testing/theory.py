# Testing
# The first level of software testing
# The smallest testable parts of a software are tested
# Validates that each unit of the software performs as designed
# Types of testing:
# Manual testing
# Automated testing
# Unit testing
# Integration testing
# Many more types of testing

# What is manual testing?
# Manually test the code as a standard user
# Go to each page of a web application
# Test every behavior and functionality
# And this happens every time
# A new feature is introduced
# A bug is fixed
# A requirement is changed

# Drawbacks from Manual Testing
# Not repeatable
# Automatically. Changing part of the code
# Hard to structure
# Depends on the manual tester
# Less accuracy
# The possibility of "human error" is applicable here
# Not as easy as it should be
# Requires more time and resources

# Automated testing
# Automated testing represents business requirements in code
# i.e., code that verifies code
# Types of automated tests
# Unit tests
# Integration tests
# Functional/UI/E2E tests
# System tests
# Regression  tests
# etc..
# Done through an automation tool
# Higher accuracy
# Better reporting capabilities
# Increased coverage
# Improved bug detection
# Increased reusability
# Stability

# Benefits of automated testing
# Automated tests:
# are automatically repeatable
# fail as early as possible
# enable the presentation of business requirements in code
# reduce the cost of change
# decrease the number of defects in the code
# Bonus:
# Improve design


# Code conventions while testing
# While writing tests, different conventions and practices are used
# Less abstract, more concrete
# Test specific cases
# Triple A pattern:
# Arrange
# Act
# Assert


# UNIT TESTING
# Unit Testing is a type of software testing where individual units or components of a software are tested
# The purpose is to validate that each unit of the software code performs as expected
# Unit Testing is done during the development (coding phase) of an application by the developers


# Unit Testing Framework
# Individual units or components are being tested
# Validate each unit to perform as expected
# A unit may be an individual:
# Function
# Method
# Procedure
# Modules
# Object

# Concepts Behind unittest (1)
# Test fixture
# A baseline for running tests to ensure there is a fixed environment in which tests are run so that results are repeatable
# Test case
# A set of conditions used to determine if a system works correctly
# Test suite
# A collection of testcases used to test a software if it has some specified set of behaviors
# Test runner
# A component which sets up the execution of tests and provides the outcome to the user

# !!! ВСИЧКИ тестове трябва да започват с "test_" !!!
import unittest
class SimpleTest(unittest.TestCase):
    def test_upper(self):
        result = 'foo'.upper()
        expected_result = 'FOO'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()


# Run by the following block of code
if __name__ == '__main__':
  unittest.main()
# Results printed on the console
# ----------------------
# Ran 1 test in 0.00s
# OK  (Test outcome)

# The possible outcomes are
# OK – all tests passed
# FAIL – one or many tests failed and an AssertionError exception is raised
# ERROR – the tests raised an exception other than AssertionError

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Basic Unittest Terms (1)
# unittest.TestCase – create test cases by subclassing it
# assertEqual() / assertNotEqual() – tests that the two arguments are equal/unequal in value
# assertTrue() / assertFalse() – tests that the argument has a Boolean value of True/False
# assertIn() / assertNotIn() – tests that the first argument is in / is not in the second
# assertRaises() – raises a specific exception
# unittest.main() – provides a command-line interface to the test script
# setUp() – prepares the test fixture
# The method is called immediately before the test method

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Test Example (1)
# If we have a class Person with methods get_full_name() and get_info():
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'

# We can test both methods using the code below:
import unittest

class PersonTests(unittest.TestCase):
    def setUp(self):
        self.person = Person("Luc", "Peterson", 25)

    def test_get_full_name(self):
        result = self.person.get_full_name()
        expected_result = "Luc Peterson"
        self.assertEqual(result, expected_result)

    def test_get_info(self):
        result = self.person.get_info()
        expected_result = "Luc Peterson is 25 years old"
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

# Unittest Modules
# Advantages to placing the test code in a separate module:
# The test module can be run standalone from the command line
# The test code can more easily be separated from shipped code
# Tested code can be refactored more easily
# If the testing strategy changes, there is no need to change the source code

# Unittest Modules Example
# Testing the class Person from previous example:
# Create the tests in a separate module
# Include them in a package in order to be able to make proper imports from the modules
# import unittest
# from project.person import Person