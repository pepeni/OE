from random import randint, sample, uniform
from math import floor, ceil

from src.fitness_function import FitnessFunction
from src.individual import Individual


def get_sorted_individuals(individuals: list[Individual], look_for_max: bool) -> list[Individual]:
    return sorted(individuals, key=lambda individual: individual.fitness_value, reverse=look_for_max)


def select_random_parents(selected_individuals):
    index1, index2 = sample(range(len(selected_individuals)), 2)
    parent1 = selected_individuals[index1]
    parent2 = selected_individuals[index2]
    return parent1, parent2


class Population:
    def __init__(self, size: int, number_of_variables: int, chromosome_length: int, min_value: int, max_value: int,
                 fitness_function: FitnessFunction, epochs: int, selection_percent=0.5, elite_percent=0.1,
                 crossover_prob=0.8, mutation_prob=0.1, inversion_prob=0.05, look_for_max=False) -> None:
        self.size = size
        self.chromosome_length = chromosome_length
        self.min_value = min_value
        self.max_value = max_value
        self.fitness_function = fitness_function
        self.epochs = epochs
        self.selection_percent = selection_percent
        self.number_to_select = floor(selection_percent * size)
        self.elite_percent = elite_percent
        self.number_elite = ceil(elite_percent * self.number_to_select)
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.inversion_prob = inversion_prob
        self.look_for_max = look_for_max
        self.best_individuals = []

        self.individuals = [
            Individual(
                chromosome_length,
                min_value,
                max_value,
                fitness_function,
                [[randint(0, 1) for _ in range(chromosome_length)] for _ in range(number_of_variables)]
            )
            for _ in range(size)
        ]

        self.selection_method = None
        self.crossover_method = None
        self.mutation_method = None
        self.inversion_method = None

    def get_individual(self, index) -> Individual:
        return self.individuals[index]

    def set_individual(self, index, individual) -> None:
        self.individuals[index] = individual

    def get_size(self) -> int:
        return self.size

    def set_selection_method(self, method) -> None:
        self.selection_method = method

    def set_crossover_method(self, method) -> None:
        self.crossover_method = method

    def set_mutation_method(self, method) -> None:
        self.mutation_method = method

    def set_inversion_method(self, method) -> None:
        self.inversion_method = method

    def select_individuals(self) -> list[Individual]:
        return self.selection_method(self.individuals, self.number_to_select)

    def crossover_individuals(self, parent1: Individual, parent2: Individual) -> tuple[Individual, Individual]:
        return self.crossover_method(parent1, parent2, self.chromosome_length, self.min_value, self.max_value,
                                     self.fitness_function)

    def mutate_individual(self, individual: Individual, probability: float) -> None:
        return self.mutation_method(individual, probability)

    def invert_individual(self, individual: Individual, probability: float) -> None:
        return self.inversion_method(individual, probability)

    def get_best_individual(self):
        return get_sorted_individuals(self.individuals, self.look_for_max)[0]

    def evolve(self):
        for epoch in range(self.epochs):
            selected_individuals = self.select_individuals()
            self.individuals = []
            elite_individuals = get_sorted_individuals(selected_individuals, self.look_for_max)[:self.number_elite]

            while len(self.individuals) < self.size - self.number_elite:
                parent1, parent2 = select_random_parents(selected_individuals)
                if self.crossover_prob >= uniform(0, 1):
                    child1, child2 = self.crossover_individuals(parent1, parent2)
                    self.individuals.append(child1)
                    if len(self.individuals) == self.size - self.number_elite:
                        break
                    self.individuals.append(child2)

            for individual in self.individuals:
                self.mutate_individual(individual, self.mutation_prob)
                self.invert_individual(individual, self.inversion_prob)

            for individual in elite_individuals:
                self.individuals.append(individual)

            self.best_individuals.append(self.get_best_individual())

    def print_individuals(self):
        for ind in self.individuals:
            print(ind.__repr__(), ind.decoded_values, ind.fitness_value)

    def print_best_individuals(self):
        for i, ind in enumerate(self.best_individuals):
            print(f'Epoka {i + 1}: {ind.__repr__(), ind.decoded_values, ind.fitness_value}')

    def __str__(self):
        return "\n".join(str(individual) for individual in self.individuals)
