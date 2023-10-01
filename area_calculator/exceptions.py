class InvalidFigureParameterException(Exception):
    _message = "Size parameter of figure equal or less than zero"

    def __init__(self):
        super().__init__(self._message)


class InvalidTrainleParametersException(Exception):
    _message = "Triangle with that parameters are impossible"

    def __init__(self):
        super().__init__(self._message)
