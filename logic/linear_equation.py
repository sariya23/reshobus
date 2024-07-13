from .abstract_equation import Equation
from .templates import LinearTemplates
from .exceptions import UndefinedDifficultException


from enum import Enum


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

    def __str__(self):
        pass


# import sympy as sp
#
# # Определяем переменную x
# x = sp.symbols('x')
#
# # Уравнение в виде строки
# equation_str = "2*x=6"
#
# # Разбиваем строку на левую и правую часть
# left_str, right_str = equation_str.split('=')
#
# # Преобразуем части уравнения из строк в символьные выражения
# left_expr = sp.sympify(left_str)
# right_expr = sp.sympify(right_str)
#
# # Создаем уравнение
# equation = sp.Eq(left_expr, right_expr)
#
# # Решаем уравнение
# solution = sp.solve(equation, x)
#
# print(f"Решение уравнения: x = {solution[0]}")
