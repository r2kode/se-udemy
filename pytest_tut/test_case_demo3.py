import pytest


@pytest.fixture()
def setUp():
    print("demo3 setup")
    yield
    print("demo3 teardown")

def test_demo3_methodA(setUp):
    print("running demo3 test")

def test_demo3_methodB(setUp):
    print("running demo3 test")