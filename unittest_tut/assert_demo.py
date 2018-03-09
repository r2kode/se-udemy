import unittest


class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not true")
        b = False
        self.assertFalse(b, "b is not false")

    def test_assertEqual(self):
        a = 10
        b = 101
        self.assertEqual(a, b, "args are not equal")



if __name__ == '__main__':
    unittest.main(verbosity=2)
