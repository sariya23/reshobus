from .abstract_equation import Equation
from .templates import Templates

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
                return cls(Templates.EASY_LINEAR.value)
            case Difficult.MEDIUM:
                return cls(Templates.MEDIUM_LINEAR.value)
            case Difficult.HARD:
                return cls(Templates.HARD_LINEAR.value)
            case _:
                raise ValueError(f"Undefined difficult {difficult}")

    def generate(self):
        pass

    def __str__(self):
        pass
