import random

from P2.src.individual import Individual


class InversionMethods:
    @staticmethod
    def double_point_inversion(individual: Individual, probability: float) -> None:
        size = individual.get_chromosome_length()
        for chromosome in individual.chromosomes:
            size = individual.get_chromosome_length()
            random1 = random.randint(0, size - 1)
            random2 = random.randint(random1, size - 1)
            cross_point_1, cross_point_2 = min(random1, random2), max(random1, random2)
            random_var = random.random()
            if random_var < probability:
                chromosome.genes[cross_point_1:cross_point_2 + 1] = reversed(chromosome.genes[cross_point_1:cross_point_2 + 1])
