import unittest


class TestCase2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("- setUp TestCase 2 - run only once before tests")

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
        print("- tearDown TestCase 2 - run once after all test are done")


if __name__ == '__main__':
    unittest.main()
