import random

from src.individual import Individual


class MutationMethods:
    @staticmethod
    def edge_mutation(individual: Individual, probability: float) -> None:
        for chromosome in individual.chromosomes:
            random_var = random.random()
            if random_var < probability:
                chromosome.genes[-1] = 1 if chromosome.genes[-1] == 0 else 0

    @staticmethod
    def single_point_mutation(individual: Individual, probability: float) -> None:
        for chromosome in individual.chromosomes:
            random_var = random.random()
            if random_var < probability:
                index = random.randint(0, individual.get_chromosome_length() - 1)
                chromosome.genes[index] = 1 if chromosome.genes[index] == 0 else 0

    @staticmethod
    def double_point_mutation(individual: Individual, probability: float) -> None:
        for chromosome in individual.chromosomes:
            size = individual.get_chromosome_length()
            random_var = random.random()
            if random_var < probability:
                index1 = random.randint(0, size - 1)
                index2 = random.randint(0, size - 1)
                chromosome.genes[index1] = 1 if chromosome.genes[index1] == 0 else 0
                chromosome.genes[index2] = 1 if chromosome.genes[index2] == 0 else 0
