import unittest


class AssertDemo(unittest.TestCase):

    def test_assert_demo(self):
        a = True
        self.assertFalse(a, "'a' is not false")
        b = False
        self.assertFalse(b, "'b' is not false")


# if __name__ == '__main__':
#     unittest.main(verbosity=2)


