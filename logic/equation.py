from abc import ABC, abstractmethod


class Equation(ABC):
    UNKNOWN_VALUE = "x"

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def __str__(self):
        pass