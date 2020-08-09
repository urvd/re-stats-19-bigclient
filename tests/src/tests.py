import unittest
from tests.tests_tests.test_example_2 import RandomTest2
from tests.tests_tests.test_skeleton import RandomTest

suite = unittest.TestSuite()
suite.addTest(RandomTest())
suite.addTest(RandomTest2())

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite

    runner.run(test_suite)
