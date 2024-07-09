from .abstract_equation import Equation
from .templates import Templates
from .exceptions import UndefinedDifficultException

from enum import Enum


class Difficult(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class LinearEquation(Equation):
    def __init__(self, equation_template: str = ""):
        self.equation_template = equation_template

    @classmethod
    def from_template_with_concrete_difficult(cls, difficult: Difficult):
        match difficult:
            case Difficult.EASY:
                return cls(Templates.EASY_LINEAR)
            case Difficult.MEDIUM:
                return cls(Templates.MEDIUM_LINEAR)
            case Difficult.HARD:
                return cls(Templates.HARD_LINEAR)
            case _:
                raise UndefinedDifficultException(f"Undefined difficult {difficult}")

    def generate(self):
        pass

    def __str__(self):
        pass
