from abc import ABC, abstractmethod


class Equation(ABC):
    UNKNOWN_VALUE = "x"

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
