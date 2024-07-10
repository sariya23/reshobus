from abc import ABC, abstractmethod
from random import choice, randint

from sympy import symbols


class Equation(ABC):
    UNKNOWN_VALUE = symbols("x")
    OPERATORS = ("+", "-", "*", "/")

    def __init__(self, equation_template: str = "", *constants):
        self.equation_template = equation_template
        self.constants = constants

        self.equation = self.generate()

    def __replace_spec_signs_to_math_signs(self, equation: str) -> str:
        amount_of_sign = equation.count("<sign>")
        equation = self.equation_template

        for _ in range(amount_of_sign):
            equation = equation.replace("<sign>", choice(self.OPERATORS), 1)

        assert "<sign>" not in equation
        return equation

    @staticmethod
    def __replace_letter_coefficients_to_numbers(self, equation: str):
        equation = equation

        for constant in self.constants:
            coefficient = randint(1, 100)
            equation = equation.replace(constant, str(coefficient), 1)

        return equation

    @abstractmethod
    def generate(self):
        equation = self.__replace_spec_signs_to_math_signs(self.equation_template)
        equation = self.__replace_letter_coefficients_to_numbers(equation)

        return equation

    @abstractmethod
    def __str__(self):
        pass
