import unittest
import time
import unittest_tut.assert_demo


class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("- setUpClass - run only once before tests")

    def setUp(self):
        print("set up, run once before every test")

    def test_methodA(self):
        print("test method A")

    def test_methodB(self):
        print("test method B")

    def tearDown(self):
        print("run after every test")

    @classmethod
    def tearDownClass(cls):
        print("- tearDownClass - run once after all test are done")


if __name__ == '__main__':
    unittest.main()
