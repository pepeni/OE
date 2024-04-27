from typing import Callable


class FitnessFunction:
    def __init__(self, function: Callable[[list[float], int], float]) -> None:
        self.function = function

    def evaluate(self, values: list[float], ndim: int) -> float:
        return self.function(values, ndim)
