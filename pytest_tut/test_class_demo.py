import pytest
from pytest_tut.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abd = SomeClassToTest(10)

    def test_method_a(self):
        print("test_method_A")
        result = self.abd.sumNumbers(2, 9)
        assert result == 21

    def test_method_b(self):
        print("test method B")
