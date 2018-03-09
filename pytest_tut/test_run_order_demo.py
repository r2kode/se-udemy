import pytest


@pytest.mark.run(order=2)
def test_run_order_method_a(oneTimeSetUp, setUp):
    print("Test methof A")

@pytest.mark.run(order=6)
def test_run_order_method_b(oneTimeSetUp, setUp):
    print("Test methof B")

@pytest.mark.run(order=5)
def test_run_order_method_c(oneTimeSetUp, setUp):
    print("Test methof C")

@pytest.mark.run(order=3)
def test_run_order_method_d(oneTimeSetUp, setUp):
    print("Test methof D")

@pytest.mark.run(order=7)
def test_run_order_method_e(oneTimeSetUp, setUp):
    print("Test methof E")

@pytest.mark.run(order=1)
def test_run_order_method_f(oneTimeSetUp, setUp):
    print("Test methof F")

@pytest.mark.run(order=4)
def test_run_order_method_g(oneTimeSetUp, setUp):
    print("Test methof G")
