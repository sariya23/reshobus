from abc import ABC, abstractmethod

from sympy import symbols


class Equation(ABC):
    UNKNOWN_VALUE = symbols("x")
    OPERATORS = ("+", "-", "*", "/")

    def __init__(self, equation_template: str = "", *constants):
        self.equation_template = equation_template
        self.constants = constants

        self.equation = self.generate()

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
