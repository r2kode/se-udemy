import pytest


@pytest.fixture()
def setUp():
    print("once before every method")

def test_methodA(setUp):
    print("run test method A")


def test_methodB(setUp):
    print("run test method B")
