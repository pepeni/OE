import math
import random

from P4.src.fitness_function import FitnessFunction
from P4.src.individual import Individual


class CrossoverMethods:
    @staticmethod
    def arithmetic_crossover(parent1: Individual, parent2: Individual, min_value: float, max_value: float,
                             fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        alpha = random.random()
        genes_length = len(parent1.genes)
        child1 = []
        child2 = []
        for i in range(genes_length):
            gene1 = alpha * parent1.genes[i] + (1 - alpha) * parent2.genes[i]
            gene2 = alpha * parent2.genes[i] + (1 - alpha) * parent1.genes[i]
            child1.append(gene1)
            child2.append(gene2)
        individual_child1 = Individual(min_value, max_value, fitness_function, child1)
        individual_child2 = Individual(min_value, max_value, fitness_function, child2)
        return individual_child1, individual_child2

    @staticmethod
    def linear_crossover(parent1: Individual, parent2: Individual, min_value: float, max_value: float,
                         fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        genes_length = len(parent1.genes)
        child1 = []
        child2 = []
        child3 = []
        for i in range(genes_length):
            geneZ = (1/2) * parent1.genes[i] + (1/2) * parent2.genes[i]
            geneV = (3/2) * parent2.genes[i] - (1/2) * parent1.genes[i]
            geneX = -(1/2) * parent2.genes[i] + (3/2) * parent1.genes[i]
            child1.append(geneZ)
            child2.append(geneV)
            child3.append(geneX)
        individual_child1 = Individual(min_value, max_value, fitness_function, child1)
        individual_child2 = Individual(min_value, max_value, fitness_function, child2)
        individual_child3 = Individual(min_value, max_value, fitness_function, child3)

        fv1, fv2, fv3 = individual_child1.fitness_value, individual_child2.fitness_value, individual_child3.fitness_value

        if fv1 > fv3 and fv1 > fv2:
            return individual_child2, individual_child3
        elif fv2 > fv3:
            return individual_child1, individual_child3
        else:
            return individual_child1, individual_child2

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
        alpha = 0.25
        beta = 0.7
        genes_length = len(parent1.genes)
        child1 = []
        child2 = []
        for i in range(genes_length):
            delta = math.fabs(parent1.genes[i] - parent2.genes[i])
            a, b = min(parent1.genes[i], parent2.genes[i]), max(parent1.genes[i], parent2.genes[i])
            gene1 = random.uniform(a - delta * alpha, b + delta * beta)
            gene2 = random.uniform(a - delta * alpha, b + delta * beta)
            child1.append(gene1)
            child2.append(gene2)
        individual_child1 = Individual(min_value, max_value, fitness_function, child1)
        individual_child2 = Individual(min_value, max_value, fitness_function, child2)
        return individual_child1, individual_child2

    @staticmethod
    def averaging_crossover(parent1: Individual, parent2: Individual, min_value: float, max_value: float,
                             fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        genes_length = len(parent1.genes)
        child = []
        for i in range(genes_length):
            gene = (parent1.genes[i] + parent2.genes[i]) / 2
            child.append(gene)
        individual_child1 = Individual(min_value, max_value, fitness_function, child)
        individual_child2 = Individual(min_value, max_value, fitness_function, child)
        return individual_child1, individual_child2

    @staticmethod
    def geometric_crossover(parent1: Individual, parent2: Individual, min_value: float, max_value: float,
                             fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        genes_length = len(parent1.genes)
        child = []
        for i in range(genes_length):
            if parent1.genes[i] > 0 and parent2.genes[i] > 0:
                gene = math.sqrt(parent1.genes[i] * parent2.genes[i])
            else:
                gene = (parent1.genes[i] + parent2.genes[i]) / 2
            child.append(gene)
        individual_child1 = Individual(min_value, max_value, fitness_function, child)
        individual_child2 = Individual(min_value, max_value, fitness_function, child)
        return individual_child1, individual_child2

    @staticmethod
    def guided_crossover(parent1: Individual, parent2: Individual, min_value: float, max_value: float,
                             fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        pass

    @staticmethod
    def diverse_crossover(parent1: Individual, parent2: Individual, min_value: float, max_value: float,
                             fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        pass
