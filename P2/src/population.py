import numpy as np

from src.fitness_function import FitnessFunction
from src.individual import Individual


class Population:
    def __init__(self, size: int, number_of_variables: int, chromosome_length: int, min_value: int, max_value: int, fitness_function: FitnessFunction):
        self.size = size
        self.individuals = [Individual(number_of_variables, chromosome_length, min_value, max_value, fitness_function) for _ in range(size)]

    def get_individual(self, index):
        return self.individuals[index]

    def set_individuals(self, index, individual):
        self.individuals[index] = individual

    def get_size(self):
        return self.size

    def __str__(self):
        return "\n".join(str(individual) for individual in self.individuals)
