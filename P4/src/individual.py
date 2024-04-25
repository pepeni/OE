from src.fitness_function import FitnessFunction


class Individual:
    def __init__(self, min_value: float, max_value: float, fitness_function: FitnessFunction,
                 genes: list[float]) -> None:
        self.min_value = min_value
        self.max_value = max_value
        self.fitness_function = fitness_function
        self.genes = genes
        self.fitness_value = self.evaluate_fitness()

    def evaluate_fitness(self) -> float:
        return self.fitness_function.evaluate(self.genes)

    def get_genes(self) -> list[float]:
        return self.genes

    def __str__(self) -> str:
        return str(self.genes)

    def __repr__(self) -> list[float]:
        return self.genes
