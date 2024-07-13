import pytest

from string import ascii_letters

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


@pytest.mark.parametrize(
    "difficult",
    [
        Difficult.EASY,
        Difficult.MEDIUM,
        Difficult.HARD,
    ],
)
def test_after_generating_no_spec_signs_and_letters_in_equation(difficult):
    eq = LinearEquation().from_template_with_concrete_difficult(difficult).equation
    constant_names = ascii_letters.replace("x", "")
    assert "<sign>" not in eq
    assert all(i not in constant_names for i in eq)
