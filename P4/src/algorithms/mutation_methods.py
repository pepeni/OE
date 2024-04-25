import random
import numpy as np

from src.individual import Individual


class MutationMethods:
    @staticmethod
    def uniform_mutation(individual: Individual, probability: float, min_value: float, max_value: float) -> None:
        pass

    @staticmethod
    def index_mutation(individual: Individual, probability: float, min_value: float, max_value: float) -> None:
        pass

    @staticmethod
    def gauss_mutation(individual: Individual, probability: float, min_value: float, max_value: float) -> None:
        for i in range(len(individual.genes)):
            random_var = random.random()
            if random_var < probability:
                norm_sample = np.random.normal(0, 1, 1)
                while individual.genes[i] + norm_sample[0] < min_value or individual.genes[i] + norm_sample[0] > max_value:
                    norm_sample = np.random.normal(0, 1, 1)
                individual.genes[i] += norm_sample
