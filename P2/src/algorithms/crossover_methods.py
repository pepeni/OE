import random

from P2.src.fitness_function import FitnessFunction
from P2.src.individual import Individual


class CrossoverMethods:
    @staticmethod
    def single_point_crossover(parent1: Individual, parent2: Individual, chromosome_length: int, min_value: int,
                               max_value: int, fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        child1 = []
        child2 = []
        for chromosome1, chromosome2 in zip(parent1.chromosomes, parent2.chromosomes):
            cross_point = random.randint(0, chromosome_length - 1)
            child_chromosome_1 = []
            child_chromosome_2 = []
            for i in range(chromosome_length):
                if i <= cross_point:
                    child_chromosome_1.append(chromosome1.genes[i])
                    child_chromosome_2.append(chromosome2.genes[i])
                else:
                    child_chromosome_1.append(chromosome2.genes[i])
                    child_chromosome_2.append(chromosome1.genes[i])
            child1.append(child_chromosome_1)
            child2.append(child_chromosome_2)

        individual_child1 = Individual(chromosome_length, min_value, max_value, fitness_function, child1)
        individual_child2 = Individual(chromosome_length, min_value, max_value, fitness_function, child2)
        return individual_child1, individual_child2

    @staticmethod
    def double_point_crossover(parent1: Individual, parent2: Individual, chromosome_length: int, min_value: int,
                               max_value: int, fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        child1 = []
        child2 = []
        for chromosome1, chromosome2 in zip(parent1.chromosomes, parent2.chromosomes):
            random1 = random.randint(0, chromosome_length - 1)
            random2 = random.randint(random1, chromosome_length - 1)
            cross_point_1, cross_point_2 = min(random1, random2), max(random1, random2)
            child_chromosome_1 = []
            child_chromosome_2 = []
            for i in range(chromosome_length):
                if cross_point_1 < i <= cross_point_2:
                    child_chromosome_1.append(chromosome2.genes[i])
                    child_chromosome_2.append(chromosome1.genes[i])
                else:
                    child_chromosome_1.append(chromosome1.genes[i])
                    child_chromosome_2.append(chromosome2.genes[i])
            child1.append(child_chromosome_1)
            child2.append(child_chromosome_2)

        individual_child1 = Individual(chromosome_length, min_value, max_value, fitness_function, child1)
        individual_child2 = Individual(chromosome_length, min_value, max_value, fitness_function, child2)
        return individual_child1, individual_child2

    @staticmethod
    def triple_point_crossover(parent1: Individual, parent2: Individual, chromosome_length: int, min_value: int,
                               max_value: int, fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        child1 = []
        child2 = []
        for chromosome1, chromosome2 in zip(parent1.chromosomes, parent2.chromosomes):
            random_list = [random.randint(0, chromosome_length - 1) for _ in range(3)]
            random_list.sort()
            cross_point_1, cross_point_2, cross_point_3 = random_list[0], random_list[1], random_list[2]
            child_chromosome_1 = []
            child_chromosome_2 = []
            for i in range(chromosome_length):
                if cross_point_1 < i <= cross_point_2 or i > cross_point_3:
                    child_chromosome_1.append(chromosome2.genes[i])
                    child_chromosome_2.append(chromosome1.genes[i])
                else:
                    child_chromosome_1.append(chromosome1.genes[i])
                    child_chromosome_2.append(chromosome2.genes[i])
            child1.append(child_chromosome_1)
            child2.append(child_chromosome_2)

        individual_child1 = Individual(chromosome_length, min_value, max_value, fitness_function, child1)
        individual_child2 = Individual(chromosome_length, min_value, max_value, fitness_function, child2)
        return individual_child1, individual_child2

    @staticmethod
    def uniform_crossover(parent1: Individual, parent2: Individual, chromosome_length: int, min_value: int,
                          max_value: int, fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        child1 = []
        child2 = []
        for chromosome1, chromosome2 in zip(parent1.chromosomes, parent2.chromosomes):
            child_chromosome_1 = []
            child_chromosome_2 = []
            for i in range(chromosome_length):
                if random.random() < 0.5:
                    child_chromosome_1.append(chromosome2.genes[i])
                    child_chromosome_2.append(chromosome1.genes[i])
                else:
                    child_chromosome_1.append(chromosome1.genes[i])
                    child_chromosome_2.append(chromosome2.genes[i])
            child1.append(child_chromosome_1)
            child2.append(child_chromosome_2)

        individual_child1 = Individual(chromosome_length, min_value, max_value, fitness_function, child1)
        individual_child2 = Individual(chromosome_length, min_value, max_value, fitness_function, child2)
        return individual_child1, individual_child2

    @staticmethod
    def discrete_crossover(parent1: Individual, parent2: Individual, chromosome_length: int, min_value: int,
                           max_value: int, fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        child1 = []
        child2 = []
        for chromosome1, chromosome2 in zip(parent1.chromosomes, parent2.chromosomes):
            child_chromosome_1 = []
            child_chromosome_2 = []
            for i in range(chromosome_length):
                if random.random() > 0.5:
                    child_chromosome_1.append(chromosome2.genes[i])
                    child_chromosome_2.append(chromosome1.genes[i])
                else:
                    child_chromosome_1.append(chromosome1.genes[i])
                    child_chromosome_2.append(chromosome2.genes[i])
            child1.append(child_chromosome_1)
            child2.append(child_chromosome_2)

        individual_child1 = Individual(chromosome_length, min_value, max_value, fitness_function, child1)
        individual_child2 = Individual(chromosome_length, min_value, max_value, fitness_function, child2)
        return individual_child1, individual_child2

    @staticmethod
    def dissociated_crossover(parent1: Individual, parent2: Individual, chromosome_length: int, min_value: int,
                              max_value: int, fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        child1 = []
        child2 = []
        for chromosome1, chromosome2 in zip(parent1.chromosomes, parent2.chromosomes):
            random1 = random.randint(0, chromosome_length - 1)
            random2 = random.randint(0, chromosome_length - 1)
            cross_point_1, cross_point_2 = min(random1, random2), max(random1, random2)
            child_chromosome_1 = []
            child_chromosome_2 = []
            for i in range(chromosome_length):
                if i <= cross_point_1:
                    child_chromosome_1.append(chromosome1.genes[i])
                    child_chromosome_2.append(chromosome2.genes[i])
                elif cross_point_1 < i <= cross_point_2:
                    child_chromosome_1.append(chromosome1.genes[i] | chromosome2.genes[i])
                    child_chromosome_2.append(chromosome1.genes[i] & chromosome2.genes[i])
                else:
                    child_chromosome_1.append(chromosome2.genes[i])
                    child_chromosome_2.append(chromosome1.genes[i])
            child1.append(child_chromosome_1)
            child2.append(child_chromosome_2)

        individual_child1 = Individual(chromosome_length, min_value, max_value, fitness_function, child1)
        individual_child2 = Individual(chromosome_length, min_value, max_value, fitness_function, child2)
        return individual_child1, individual_child2

    @staticmethod
    def differences_based_crossover(parent1: Individual, parent2: Individual, chromosome_length: int, min_value: int,
                                    max_value: int, fitness_function: FitnessFunction) -> tuple[Individual, Individual]:
        child1 = []
        child2 = []
        for chromosome1, chromosome2 in zip(parent1.chromosomes, parent2.chromosomes):
            child_chromosome_1 = []
            child_chromosome_2 = []
            diff_indices = [i for i in range(chromosome_length) if chromosome1.genes[i] != chromosome2.genes[i]]
            if len(diff_indices) == 0:
                child1.append(chromosome1.genes)
                child2.append(chromosome2.genes)
            else:
                cross_point = random.choice(diff_indices)
                for i in range(chromosome_length):
                    if i >= cross_point:
                        child_chromosome_1.append(chromosome2.genes[i])
                        child_chromosome_2.append(chromosome1.genes[i])
                    else:
                        child_chromosome_1.append(chromosome1.genes[i])
                        child_chromosome_2.append(chromosome2.genes[i])
                child1.append(child_chromosome_1)
                child2.append(child_chromosome_2)

        individual_child1 = Individual(chromosome_length, min_value, max_value, fitness_function, child1)
        individual_child2 = Individual(chromosome_length, min_value, max_value, fitness_function, child2)
        return individual_child1, individual_child2
