import random

from P4.src.individual import Individual


class InversionMethods:
    @staticmethod
    def simple_inversion(individual: Individual, probability: float) -> None:
        size = len(individual.genes)
        random1 = random.randint(0, size - 1)
        random2 = random.randint(0, size - 1)
        cross_point_1, cross_point_2 = min(random1, random2), max(random1, random2)
        random_var = random.random()
        if random_var < probability:
            individual.genes[cross_point_1:cross_point_2 + 1] = reversed(
                individual.genes[cross_point_1:cross_point_2 + 1])
