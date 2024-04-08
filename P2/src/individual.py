from P2.src.chromosome import Chromosome
from P2.src.fitness_function import FitnessFunction


class Individual:
    def __init__(self, chromosome_length: int, min_value: int, max_value: int, fitness_function: FitnessFunction,
                 chromosomes: list[list[int]]) -> None:
        self.chromosome_length = chromosome_length
        self.min_value = min_value
        self.max_value = max_value
        self.fitness_function = fitness_function
        self.chromosomes = [Chromosome(self.chromosome_length, chromosomes[i]) for i in range(len(chromosomes))]
        self.decoded_values = self.decode_chromosome()
        self.fitness_value = self.evaluate_fitness()

    def decode_chromosome(self) -> list[float]:
        return [self.binary_to_decimal(chromosome) for chromosome in self.chromosomes]

    def binary_to_decimal(self, chromosome: Chromosome) -> float:
        decimal_value = int(''.join(map(str, chromosome.genes)), 2)
        scaled_value = self.min_value + decimal_value * (self.max_value - self.min_value) / (
                    2 ** len(chromosome.genes) - 1)
        return scaled_value

    def evaluate_fitness(self) -> float:
        return self.fitness_function.evaluate(self.decoded_values)

    def get_chromosome_length(self) -> int:
        return self.chromosome_length

    def get_chromosomes(self) -> list[Chromosome]:
        return self.chromosomes

    def __str__(self) -> str:
        return "\n".join(str(chromosome) for chromosome in self.chromosomes)

    def __repr__(self) -> list[list[int]]:
        return [chromosome.__repr__() for chromosome in self.chromosomes]
