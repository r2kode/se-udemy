import pytest


@pytest.yield_fixture()
def setUp():
    print("once before every method")
    yield
    print("after test method")

def test_methodA(setUp):
    print("run method a")

def test_methodB(setUp):
    print("run method B")