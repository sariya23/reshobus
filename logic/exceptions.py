class EquationCreateException(BaseException):
    pass


class UndefinedDifficultException(EquationCreateException):
    pass


class ValidationErrorUserTemplate(EquationCreateException):
    pass


class NoSpecSigns(ValidationErrorUserTemplate):
    pass


class UnexpectedConstant(ValidationErrorUserTemplate):
    pass
