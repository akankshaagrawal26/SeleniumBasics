import pytest


# Whatever written after yield runs once after every method
#After pytest version 2.10, you do not need @pytest.yield_fixture() explicitly to use yield.
#The default @pytest.fixture() also supports yield.
@pytest.yield_fixture()
def set_up():
    print("Rum once before every method")
    yield
    print("Rum once after every method")


def test_method1(set_up):
    print("This is methodA")


def test_method2(set_up):
    print("This is methodB")

