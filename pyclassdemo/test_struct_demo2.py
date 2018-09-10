import pytest
from pyclassdemo.structuring_demo import StructuringDemo


@pytest.mark.usefixtures("set_up_once", "set_up")
class TestStructuringDemo:

    @pytest.fixture(autouse=True)
    def class_setup(self, set_up_once):
        self.abc = StructuringDemo(self.value)

    def test_method1(self):
        res = self.abc.add(2, 8)
        assert res == 20
        print("This is methodA")

    def test_method2(self):
        print("This is methodB")
