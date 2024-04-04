from src.chromosome import Chromosome
from src.fitness_function import FitnessFunction


class Individual:
    def __init__(self, number_of_variables: int, chromosome_length: int, min_value: int, max_value: int, fitness_function: FitnessFunction):
        self.number_of_variables = number_of_variables
        self.min_value = min_value
        self.max_value = max_value
        self.chromosomes = [Chromosome(chromosome_length) for _ in range(number_of_variables)]
        self.decoded_values = self.decode_chromosome()
        self.fitness_function = fitness_function
        self.fitness_value = self.evaluate_fitness()

    def decode_chromosome(self) -> list[float]:
        return [self.binary_to_decimal(chromosome) for chromosome in self.chromosomes]

    def binary_to_decimal(self, chromosome: Chromosome) -> float:
        decimal_value = int(''.join(map(str, chromosome.genes)), 2)
        scaled_value = self.min_value + decimal_value * (self.max_value - self.min_value) / (2 ** len(chromosome.genes) - 1)
        return scaled_value

    def evaluate_fitness(self) -> float:
        return self.fitness_function.evaluate(self.decoded_values)

    def __str__(self):
        return "\n".join(str(chromosome) for chromosome in self.chromosomes)

    def __repr__(self):
        return [chromosome.__repr__() for chromosome in self.chromosomes]
