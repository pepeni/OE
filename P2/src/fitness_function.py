
class FitnessFunction:
    def __init__(self, function):
        self.function = function

    def evaluate(self, values: list[float]):
        return self.function(values)
