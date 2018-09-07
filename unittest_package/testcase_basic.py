import unittest


class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*" * 20)
        print("Run only once before test")
        print("*" * 20)

    def setUp(self):
        print("Run before every test")

    def test_methodA(self):
        print("Execute methodA")

    def test_methodB(self):
        print("Execute methodB")

    def tearDown(self):
        print("Run after every test")

    @classmethod
    def tearDownClass(cls):
        print("*" * 20)
        print("Run only once after test")
        print("*" * 20)

#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
