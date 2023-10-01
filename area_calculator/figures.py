from abc import ABC, abstractmethod
from math import pi, sqrt
from exceptions import InvalidFigureParameterException,\
    InvalidTrainleParametersException


class Figure(ABC):

    @abstractmethod
    def get_area():
        pass


class Circle(Figure):
    _radius = 0

    def __init__(self, radius: float):
        if radius <= 0:
            raise InvalidFigureParameterException()

        self._radius = radius

    def get_area(self):
        return pi * pow(self._radius, 2)


class Triangle(Figure):
    _sides = []

    def __init__(self, side1: float, side2: float, side3: float):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise InvalidFigureParameterException()

        if not self._is_possible(side1, side2, side3):
            raise InvalidTrainleParametersException()

        self._sides = [side1, side2, side3]

    def _is_possible(self, side1: float, side2: float, side3: float):
        if side1 + side2 > side3 and\
           side1 + side3 > side2 and\
           side2 + side3 > side1:
            return True

        return False

    def get_area(self):
        p = sum(self._sides)/2
        mul = p
        for s in self._sides:
            mul *= (p - s)

        return sqrt(mul)

    def is_rectangular(self) -> bool:
        max_side = max(self._sides)
        return pow(max_side, 2) * 2 == sum([pow(s, 2) for s in self._sides])
