from .abstract_equation import Equation
from .templates import LinearTemplates
from .exceptions import UndefinedDifficultException, UnexpectedConstant, NoSpecSigns

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

    @classmethod
    def from_user_template(cls, user_template: str, *constants):
        equation_constants = user_template.split()

        if "=" not in equation_constants or "<sign>" not in equation_constants:
            raise NoSpecSigns(
                "Please check guide for user template <here(url)>.\nYou are not specify one 'equal' sign or math sign"
            )

        equation_blocks = [
            block for block in equation_constants if block not in ("<sign>", "=")
        ]

        for constant in constants:
            if constant not in equation_blocks:
                raise UnexpectedConstant(f"Unexpected constant: {constant}")

    def generate(self):
        pass

    def __str__(self):
        pass
