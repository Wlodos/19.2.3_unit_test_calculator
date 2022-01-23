import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 4, 2) == 8

    def test_division_correctly(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self, 10, 2) == 8

    def test_adding_correctly(self):
        assert self.calc.adding(self, 3, 4) == 7
