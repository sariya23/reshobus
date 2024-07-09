from dataclasses import dataclass


@dataclass
class LinearEquation:
    template: str
    constants: tuple[str, ...]


class LinearConstant:
    EASY_CONSTANT = ("a", "answer")
    MEDIUM_CONSTANT = ("a", "b", "answer")
    HARD_CONSTANT = ("a", "b", "c", "answer")


class LinearTemplates:
    EASY_LINEAR = LinearEquation("a<sign>x=answer", LinearConstant.EASY_CONSTANT)
    MEDIUM_LINEAR = LinearEquation(
        "a<sign>(b<sign>x)=answer", LinearConstant.MEDIUM_CONSTANT
    )
    HARD_LINEAR = LinearEquation(
        "(a<sign>x)<sign>(b<sign>d)=answer", LinearConstant.HARD_CONSTANT
    )
