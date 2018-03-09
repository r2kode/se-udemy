import unittest


class TestCase1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("- setUp TestCase 1 - run only once before tests")

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
        print("- tearDown TestCase 1 - run once after all test are done")


if __name__ == '__main__':
    unittest.main()
