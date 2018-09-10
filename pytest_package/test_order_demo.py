# for ordering --> pip3 install ordering
# By default it runs in alphabetically order
import pytest

# C, A, B
@pytest.mark.run(order=2)
def test_method1(set_up_once, set_up):
    print("This is demo1 methodA")


@pytest.mark.run(order=3)
def test_method2(set_up_once, set_up):
    print("This is demo1 methodB")


@pytest.mark.run(order=1)
def test_method3(set_up_once, set_up):
    print("This is demo1 methodC")
