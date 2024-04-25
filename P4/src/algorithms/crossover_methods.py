import math
import random

from src.fitness_function import FitnessFunction
from src.individual import Individual


class CrossoverMethods:
    @staticmethod
    def arithmetic_crossover(parent1: Individual, parent2: Individual, min_value: float, max_value: float,
                             fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        pass

    @staticmethod
    def linear_crossover(parent1: Individual, parent2: Individual, min_value: float, max_value: float,
                         fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        pass

    @staticmethod
    def mixed_alfa_crossover(parent1: Individual, parent2: Individual, min_value: float, max_value: float,
                             fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        alpha = 0.25
        genes_length = len(parent1.genes)
        child1 = []
        child2 = []
        for i in range(genes_length):
            delta = math.fabs(parent1.genes[i] - parent2.genes[i])
            a, b = min(parent1.genes[i], parent2.genes[i]), max(parent1.genes[i], parent2.genes[i])
            gene1 = random.uniform(a - delta * alpha, b + delta * alpha)
            gene2 = random.uniform(a - delta * alpha, b + delta * alpha)
            child1.append(gene1)
            child2.append(gene2)
        individual_child1 = Individual(min_value, max_value, fitness_function, child1)
        individual_child2 = Individual(min_value, max_value, fitness_function, child2)
        return individual_child1, individual_child2

    @staticmethod
    def mixed_alfa_beta_crossover(parent1: Individual, parent2: Individual, min_value: float, max_value: float,
                             fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        pass

    @staticmethod
    def averaging_crossover(parent1: Individual, parent2: Individual, min_value: float, max_value: float,
                             fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        pass

    @staticmethod
    def geometric_crossover(parent1: Individual, parent2: Individual, min_value: float, max_value: float,
                             fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        pass

    @staticmethod
    def guided_crossover(parent1: Individual, parent2: Individual, min_value: float, max_value: float,
                             fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        pass

    @staticmethod
    def diverse_crossover(parent1: Individual, parent2: Individual, min_value: float, max_value: float,
                             fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        pass
