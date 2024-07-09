from .abstract_equation import Equation
from .templates import LinearTemplates
from .exceptions import UndefinedDifficultException


from enum import Enum
from random import choice


class Difficult(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class LinearEquation(Equation):
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

    def __replace_spec_signs_to_concrete_math_signs(self):
        amount_of_sign = self.equation_template.count("<sign>")
        equation = self.equation_template

        for _ in range(amount_of_sign):
            equation = equation.replace("<sign>", choice(self.OPERATORS), 1)

        assert "<sign>" not in equation
        return equation

    def generate(self) -> str:
        pass

    def __str__(self):
        pass
