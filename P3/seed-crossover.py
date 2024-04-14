import math
import random


def mixed_crossover(parent1: list[float], parent2: list[float]) -> list[float]:
    size = len(parent1)
    alpha = 0.25
    child = []
    for i in range(size):
        delta = math.fabs(parent1[i] - parent2[i])
        a, b = min(parent1[i], parent2[i]), max(parent1[i], parent2[i])
        gene = random.uniform(a - delta * alpha, b + delta * alpha)
        child.append(gene)
    return child


def seed_crossover(parents: list[list[float]]) -> list[float]:
    child = mixed_crossover(parents[0], parents[1])

    if len(parents) > 2:
        for i in range(2, len(parents)):
            child = mixed_crossover(child, parents[i])

    return child
