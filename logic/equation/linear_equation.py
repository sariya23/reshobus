from logic.equation.abstract_equation import Equation
from logic.templates import LinearTemplates
from logic.exceptions import UndefinedDifficultException


from enum import Enum


class Difficult(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class LinearEquation(Equation):
    def __init__(self, equation_template: str = "", *constants):
        super().__init__(equation_template, *constants)
        self.answer = self.solve()[0]

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

    def __str__(self):
        pass


if __name__ == "__main__":
    eq = LinearEquation.from_template_with_concrete_difficult(Difficult.EASY)
    print(eq.equation)
    print(eq.solve())
