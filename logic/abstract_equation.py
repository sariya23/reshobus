from abc import ABC, abstractmethod
from random import choice

from sympy import symbols


class Equation(ABC):
    UNKNOWN_VALUE = symbols("x")
    OPERATORS = ("+", "-", "*", "/")

    def __init__(self, equation_template: str = "", *constants):
        self.equation_template = equation_template
        self.constants = constants

        self.equation = self.generate()

    def __replace_spec_signs_to_concrete_math_signs(self):
        amount_of_sign = self.equation_template.count("<sign>")
        equation = self.equation_template

        for _ in range(amount_of_sign):
            equation = equation.replace("<sign>", choice(self.OPERATORS), 1)

        assert "<sign>" not in equation
        return equation

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
