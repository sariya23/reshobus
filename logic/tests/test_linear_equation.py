import pytest

from logic.linear_equation import LinearEquation, Difficult
from logic.templates import Templates
from logic.exceptions import UndefinedDifficultException


@pytest.mark.parametrize(
    "difficult,template",
    [
        (Difficult.EASY, Templates.EASY_LINEAR),
        (Difficult.MEDIUM, Templates.MEDIUM_LINEAR),
        (Difficult.HARD, Templates.HARD_LINEAR),
    ],
)
def test_equation_created_from_template(difficult: Difficult, template: str):
    eq = LinearEquation.from_template_with_concrete_difficult(difficult)

    assert eq.equation_template == template


def test_undefined_difficult_raises_exception():
    with pytest.raises(UndefinedDifficultException):
        _ = LinearEquation.from_template_with_concrete_difficult("aboba")
