import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 2) == 3

    def test_adding_subtraction(self):
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_adding_division(self):
        assert self.calc.division(self, 9, 3) == 3

    def test_adding_multiply(self):
        assert self.calc.multiply(self, 1, 3) == 3



    def teardown(self):
        print('Выполнение метода Teardown')