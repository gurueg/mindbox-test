import pytest
from exceptions import InvalidFigureParameterException,\
    InvalidTrainleParametersException
from figures import Circle, Triangle


def test_invalid_values():
    with pytest.raises(InvalidFigureParameterException):
        Circle(-10)

    with pytest.raises(InvalidFigureParameterException):
        Triangle(-10, 1, 1)

    with pytest.raises(InvalidFigureParameterException):
        Triangle(1, -10, 1)

    with pytest.raises(InvalidFigureParameterException):
        Triangle(1, 1, -10)

    with pytest.raises(InvalidTrainleParametersException):
        Triangle(4, 5, 10)


def test_circle_area():
    assert Circle(10).get_area() == 314.1592653589793


def test_triangle_area():
    assert Triangle(3, 4, 5).get_area() == 6


def test_rectangular_trinangle():
    assert Triangle(3, 4, 5).is_rectangular()
    assert Triangle(3, 4, 6).is_rectangular() == False
