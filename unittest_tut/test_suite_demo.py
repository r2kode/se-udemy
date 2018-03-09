import unittest
from unittest_tut.test_class_1 import TestCase1
from unittest_tut.test_class_2 import TestCase2

# to run this shit from terminal
# export PYTHONPATH=$PYTHONPATH:.

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)

smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner().run(smoke_test)
