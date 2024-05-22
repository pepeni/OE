import pygad
import numpy as np
from opfunu import cec_based

from P5.src.aggreate_results import summary
from P5.src.algorithms.crossover_methods_binary import difference_based_crossover, dissociated_crossover
from P5.src.on_generation_method import on_generation

min_value = -100.0
max_value = 100.0
num_genes = 10


def decode_individual(solution: list[int]) -> list[float]:
    gene_length = len(solution) // num_genes
    genes = [solution[i * gene_length: (i + 1) * gene_length] for i in range(num_genes)]
    return [binary_to_decimal(chromosome) for chromosome in genes]


def binary_to_decimal(chromosome: list[int]) -> float:
    decimal_value = int(''.join(map(str, chromosome)), 2)
    scaled_value = min_value + decimal_value * (max_value - min_value) / (2 ** len(chromosome) - 1)
    return scaled_value


def goldstein_and_price_binary(ga_instance, solution: list[int], solution_idx) -> float:
    x0, x1 = decode_individual(solution)
    term1 = 1.0 + (x0 + x1 + 1.0) ** 2 * (19.0 - 14.0 * x0 + 3.0 * x0 ** 2 - 14.0 * x1 + 6.0 * x0 * x1 + 3.0 * x1 ** 2)
    term2 = 30.0 + (2.0 * x0 - 3.0 * x1) ** 2 * (
                18.0 - 32.0 * x0 + 12.0 * x0 ** 2 + 48.0 * x1 - 36.0 * x0 * x1 + 27.0 * x1 ** 2)
    fitness = term1 * term2
    return 1./fitness


def weierstrass_binary(ga_instance, solution: list[int], solution_idx) -> float:
    # ndim in [10, 20, 30, 50, 100]
    func = cec_based.cec2014.F62014(ndim=num_genes)
    fitness = func.evaluate(np.array(decode_individual(solution)))
    return 1./fitness


fitness_functions = {
    "goldstein_and_price_binary": goldstein_and_price_binary,
    "weierstrass_binary": weierstrass_binary
}

selection_methods = {
    "tournament": "tournament",
    "rws": "rws",
    "random": "random"
}

crossover_methods = {
    "single_point": "single_point",
    "two_points": "two_points",
    "uniform": "uniform",
    "difference_based": difference_based_crossover,
    "dissociated": dissociated_crossover
}

mutation_methods = {
    "random": "random",
    "swap": "swap"
}


if __name__ == '__main__':
    init_range_low = 0
    init_range_high = 2
    gene_type = int
    bits_number = 10

    num_generations = 50
    sol_per_pop = 60
    num_parents_mating = 30
    mutation_num_genes = 1

    ga_instance = pygad.GA(
        keep_elitism=1,
        gene_type=gene_type,
        init_range_low=init_range_low,
        init_range_high=init_range_high,
        num_genes=num_genes * bits_number,
        num_generations=num_generations,
        sol_per_pop=sol_per_pop,
        num_parents_mating=num_parents_mating,
        mutation_num_genes=mutation_num_genes,
        fitness_func=fitness_functions["weierstrass_binary"],
        parent_selection_type=selection_methods["random"],
        crossover_type=crossover_methods["single_point"],
        mutation_type=mutation_methods["random"],
        on_generation=on_generation,
        K_tournament=3,
    )

    ga_instance.run()
    summary(ga_instance)
