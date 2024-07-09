from .abstract_equation import Equation
from .templates import LinearTemplates
from .exceptions import UndefinedDifficultException

from enum import Enum


class Difficult(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class LinearEquation(Equation):
    def __init__(self, equation_template: str = "", *constants):
        self.equation_template = equation_template
        self.constants = constants

    @classmethod
    def from_template_with_concrete_difficult(cls, difficult: Difficult):
        match difficult:
            case Difficult.EASY:
                return cls(
                    LinearTemplates.EASY_LINEAR.template,
                    *LinearTemplates.EASY_LINEAR.constants,
                )
            case Difficult.MEDIUM:
                return cls(
                    LinearTemplates.MEDIUM_LINEAR.template,
                    *LinearTemplates.MEDIUM_LINEAR.constants,
                )
            case Difficult.HARD:
                return cls(
                    LinearTemplates.HARD_LINEAR.template,
                    *LinearTemplates.HARD_LINEAR.constants,
                )
            case _:
                raise UndefinedDifficultException(f"Undefined difficult {difficult}")

    def generate(self):
        pass

    def __str__(self):
        pass
