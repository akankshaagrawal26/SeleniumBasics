import pytest


# To use fixture just pass the name of the method. It runs once before the method
# By default scope is function. 
@pytest.fixture()  # decorator
def set_up():
    print("Rum once before every method")


def test_method1(set_up):
    print("This is methodA")


def test_method2():
    print("This is methodB")

