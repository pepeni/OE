from random import sample, uniform
from math import floor, ceil
from typing import Callable

import matplotlib.pyplot as plt
import statistics
import numpy as np
import os

from P4.src.fitness_function import FitnessFunction
from P4.src.individual import Individual


def get_sorted_individuals(individuals: list[Individual], look_for_max: bool) -> list[Individual]:
    return sorted(individuals, key=lambda individual: individual.fitness_value, reverse=look_for_max)


def select_random_parents(individuals: list[Individual]) -> tuple[Individual, Individual]:
    index1, index2 = sample(range(len(individuals)), 2)
    parent1 = individuals[index1]
    parent2 = individuals[index2]
    return parent1, parent2


class Population:
    def __init__(self, size: int, number_of_variables: int, min_value: float, max_value: float,
                 fitness_function: FitnessFunction, epochs: int, selection_percent=0.5, elite_percent=0.1,
                 crossover_prob=0.8, mutation_prob=0.1, inversion_prob=0.05, look_for_max=False) -> None:
        self.size = size
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
        self.best_individuals: list[Individual] = []
        self.average_values: list[float] = []
        self.std_deviation_values: list[float] = []

        self.individuals = [
            Individual(
                min_value,
                max_value,
                fitness_function,
                [uniform(min_value, max_value) for _ in range(number_of_variables)]
            )
            for _ in range(size)
        ]
        self.elite_individuals = None

        self.selection_method: Callable[[list[Individual], int, bool], list[Individual]] | None = None
        self.crossover_method: Callable[[Individual, Individual, float, float, FitnessFunction], tuple[Individual, Individual]] | None = None
        self.mutation_method: Callable[[Individual, float, float, float], None] | None = None
        self.inversion_method: Callable[[Individual, float], None] | None = None

    def get_individual(self, index) -> Individual:
        return self.individuals[index]

    def set_individual(self, index, individual: Individual) -> None:
        self.individuals[index] = individual

    def get_size(self) -> int:
        return self.size

    def set_selection_method(self, method: Callable[[list[Individual], int, bool], list[Individual]]) -> None:
        self.selection_method = method

    def set_crossover_method(self, method: Callable[[Individual, Individual, float, float, FitnessFunction], tuple[Individual, Individual]]) -> None:
        self.crossover_method = method

    def set_mutation_method(self, method: Callable[[Individual, float, float, float], None]) -> None:
        self.mutation_method = method

    def set_inversion_method(self, method: Callable[[Individual, float], None]) -> None:
        self.inversion_method = method

    def select_individuals(self) -> list[Individual]:
        return self.selection_method(self.individuals, self.number_to_select, self.look_for_max)

    def crossover_individuals(self, parent1: Individual, parent2: Individual) -> tuple[Individual, Individual]:
        return self.crossover_method(parent1, parent2, self.min_value, self.max_value, self.fitness_function)

    def mutate_individual(self, individual: Individual, probability: float) -> None:
        return self.mutation_method(individual, probability, self.min_value, self.max_value)

    def invert_individual(self, individual: Individual, probability: float) -> None:
        return self.inversion_method(individual, probability)

    def get_best_individual(self) -> Individual:
        return get_sorted_individuals(self.individuals, self.look_for_max)[0]

    def set_elite_individuals(self) -> None:
        sorted_individuals = get_sorted_individuals(self.individuals, self.look_for_max)
        self.elite_individuals = sorted_individuals[:self.number_elite]
        self.individuals = sorted_individuals[self.number_elite:]

    def save_to_file_every_iteration(self, output_file="output_data/iterations/results.txt") -> None:
        with open(output_file, 'w') as f:
            f.write("Iteration,Fitness,MeanFitness,StdDeviation\n")
            for epoch in range(self.epochs):
                f.write(
                    f"{epoch + 1},{self.best_individuals[epoch].fitness_value},{self.average_values[epoch]},{self.std_deviation_values[epoch]}\n")

    def evolve(self) -> None:
        for epoch in range(self.epochs):
            self.set_elite_individuals()
            selected_individuals = self.select_individuals()
            self.individuals = []

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

            for individual in self.elite_individuals:
                self.individuals.append(individual)

            self.best_individuals.append(self.get_best_individual())

            current_fitness_values = [individual.fitness_value for individual in self.individuals]

            average_value = statistics.mean(current_fitness_values)
            self.average_values.append(average_value)

            std_deviation = statistics.stdev(current_fitness_values)
            self.std_deviation_values.append(std_deviation)

    def print_individuals(self) -> None:
        for ind in self.individuals:
            print(ind.__repr__(), ind.genes, ind.fitness_value)

    def print_best_individuals(self) -> None:
        for i, ind in enumerate(self.best_individuals):
            print(f'Epoka {i + 1}: {ind.__repr__(), ind.genes, ind.fitness_value}')

    def plot_iteration_values(self) -> None:
        iterations = range(1, len(self.average_values) + 1)
        plt.plot(iterations, [individual.fitness_value for individual in self.best_individuals],
                 label='Najlepsza wartość funkcji')
        plt.xlabel('Iteracja')
        plt.ylabel('Wartość')
        plt.title('Najlepsza wartość funkcji od kolejnej iteracji')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join("output_data/plots", "best_fitness.png"))
        plt.show()

    def plot_average_and_std_deviation(self) -> None:
        iterations = range(1, len(self.average_values) + 1)
        plt.plot(iterations, self.average_values, label='Średnia wartość funkcji')
        plt.fill_between(iterations,
                         np.subtract(self.average_values, self.std_deviation_values),
                         np.add(self.average_values, self.std_deviation_values),
                         color='gray', alpha=0.2, label='Odchylenie standardowe')
        plt.xlabel('Iteracja')
        plt.ylabel('Wartość')
        plt.title('Średnia wartość funkcji i odchylenie standardowe od kolejnej iteracji')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join("output_data/plots", "average_std_deviation.png"))
        plt.show()

    def __str__(self) -> str:
        return "\n".join(str(individual) for individual in self.individuals)
