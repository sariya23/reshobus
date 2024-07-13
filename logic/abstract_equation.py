from abc import ABC, abstractmethod
from random import choice, randint

import sympy as sp


class Equation(ABC):
    UNKNOWN_STRING = "x"
    UNKNOWN_SYMBOL = sp.symbols(UNKNOWN_STRING)
    OPERATORS = ("+", "-", "*", "/")
    SPEC_SIGN = "<sign>"

    def __init__(self, equation_template: str = "", *constants):
        self.equation_template = equation_template
        self.constants = constants

        self.equation = self.generate()

    def __replace_spec_signs_to_math_signs(self, equation: str) -> str:
        amount_of_sign = equation.count(self.SPEC_SIGN)
        equation = self.equation_template

        for _ in range(amount_of_sign):
            equation = equation.replace(self.SPEC_SIGN, choice(self.OPERATORS), 1)

        return equation

    def __replace_letter_coefficients_to_numbers(self, equation: str) -> str:
        for constant in self.constants:
            coefficient = randint(1, 100)
            equation = equation.replace(constant, str(coefficient), 1)

        return equation

    def generate(self) -> str:
        equation_with_replaced_spec_sign = self.__replace_spec_signs_to_math_signs(
            self.equation_template
        )
        equation = self.__replace_letter_coefficients_to_numbers(
            equation_with_replaced_spec_sign
        )
        return equation

    def solve(self):
        lest_side, right_side = self.equation.split("=")
        left_expression = sp.sympify(lest_side)
        right_expression = sp.sympify(right_side)
        equation = sp.Eq(left_expression, right_expression)
        solution = sp.solve(equation, self.UNKNOWN_SYMBOL)
        return solution

    @abstractmethod
    def __str__(self):
        pass
