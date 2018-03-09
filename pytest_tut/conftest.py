import pytest


@pytest.fixture()
def setUp():
    print("running conftest method setup")
    yield
    print("running conftest method tearDown")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser, osType):
    print("one time setUP")
    if browser == "FF":
        value = 10
        print("run test on Firefox")
    else:
        value = 20
        print("Run test on default browser (Chrome)")
    if request.cls is not None:
        request.cls.value = value
    yield value
    print("one time teardown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type os operating system")
    parser.addoption("--value")

@pytest.fixture(scope="class")
def valueSetUp(request):
    return request.config.getoption("--value")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
