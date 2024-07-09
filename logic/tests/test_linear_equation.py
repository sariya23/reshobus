import pytest

from logic.linear_equation import LinearEquation, Difficult
from logic.templates import LinearTemplates
from logic.exceptions import UndefinedDifficultException


@pytest.mark.parametrize(
    "difficult,template,constants",
    [
        (
            Difficult.EASY,
            LinearTemplates.EASY_LINEAR.template,
            LinearTemplates.EASY_LINEAR.constants,
        ),
        (
            Difficult.MEDIUM,
            LinearTemplates.MEDIUM_LINEAR.template,
            LinearTemplates.MEDIUM_LINEAR.constants,
        ),
        (
            Difficult.HARD,
            LinearTemplates.HARD_LINEAR.template,
            LinearTemplates.HARD_LINEAR.constants,
        ),
    ],
)
def test_equation_created_from_template(
    difficult: Difficult, template: str, constants: tuple[str, ...]
):
    eq = LinearEquation.from_template_with_concrete_difficult(difficult)

    assert eq.equation_template == template
    assert eq.constants == constants


def test_undefined_difficult_raises_exception():
    with pytest.raises(UndefinedDifficultException):
        _ = LinearEquation.from_template_with_concrete_difficult("aboba")
