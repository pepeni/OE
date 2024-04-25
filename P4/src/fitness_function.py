
class FitnessFunction:
    def __init__(self, function) -> None:
        self.function = function

    def evaluate(self, values: list[float]) -> float:
        return self.function(values)
