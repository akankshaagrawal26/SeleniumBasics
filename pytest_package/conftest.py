import pytest


# By default scope is function
@pytest.fixture()
def set_up():
    print("Run once before every method")
    yield
    print("Run once after every method")


# Scope set to module
@pytest.fixture(scope="class")
def set_up_once(browser, os_type):
    print("Run once before every module")
    if browser == 'firefox':
        print("Run on ff")
        print(os_type)
    else:
        print("Run on chrome")
        print(os_type)
    yield
    print("Run once after every module")

# for command line arguments


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of OS")


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='session')
def os_type(request):
    return request.config.getoption("--osType")