import pytest
from pytest_tut.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestReportingDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_method_a(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("test method A")

    def test_method_b(self):
        result = self.abc.sumNumbers(2, 8)
        assert result > 20
        print("test method B")
