import pytest
from pytest_tut.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo2():

    @pytest.fixture(autouse=True)
    def classSetup(self, valueSetUp):
        self.abc = SomeClassToTest(self.value)

    def test_method_a(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("test method a")

    def test_method_b(self):
        print("test method B")
