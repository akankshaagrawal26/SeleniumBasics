import unittest
from unittest_package.assert_demo import AssertDemo
from unittest_package.testcase_basic import TestCaseDemo


tc1 = unittest.TestLoader().loadTestsFromTestCase(AssertDemo)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo)

suite_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(suite_test)