import pygad
import numpy as np
from opfunu import cec_based

from P5.src.aggreate_results import summary
from P5.src.algorithms.crossover_methods_real import arithmetic_crossover, linear_crossover, mixed_alfa_crossover, \
    mixed_alfa_beta_crossover, averaging_crossover, geometric_crossover, diverse_crossover
from P5.src.algorithms.mutation_methods_real import gauss_mutation
from P5.src.on_generation import on_generation, create_directories, do_plots


def goldstein_and_price_real(ga_instance, solution: list[float], solution_idx) -> float:
    if len(solution) != 2:
        raise AttributeError
    x0, x1 = solution
    term1 = 1.0 + (x0 + x1 + 1.0) ** 2 * (19.0 - 14.0 * x0 + 3.0 * x0 ** 2 - 14.0 * x1 + 6.0 * x0 * x1 + 3.0 * x1 ** 2)
    term2 = 30.0 + (2.0 * x0 - 3.0 * x1) ** 2 * (
                18.0 - 32.0 * x0 + 12.0 * x0 ** 2 + 48.0 * x1 - 36.0 * x0 * x1 + 27.0 * x1 ** 2)
    fitness = term1 * term2
    return 1./fitness


def weierstrass_real(ga_instance, solution: list[float], solution_idx) -> float:
    ndim = len(solution)
    if ndim not in [10, 20, 30, 50, 100]:
        raise AttributeError
    func = cec_based.cec2014.F62014(ndim=ndim)
    fitness = func.evaluate(np.array(solution))
    return 1./fitness


fitness_functions = {
    "goldstein_and_price_real": goldstein_and_price_real,
    "weierstrass_real": weierstrass_real
}

selection_methods = {
    "tournament": "tournament",
    "rws": "rws",
    "random": "random"
}

crossover_methods = {
    "arithmetic": arithmetic_crossover,
    "linear": linear_crossover,
    "mixed_alfa": mixed_alfa_crossover,
    "mixed_alfa_beta": mixed_alfa_beta_crossover,
    "averaging": averaging_crossover,
    "geometric": geometric_crossover,
    "diverse": diverse_crossover
}

mutation_methods = {
    "random": "random",
    "swap": "swap",
    "gauss": gauss_mutation
}

if __name__ == '__main__':
    min_value = -100.0
    max_value = 100.0
    num_genes = 10

    num_generations = 100
    sol_per_pop = 100
    num_parents_mating = 60
    mutation_num_genes = 1

    ga_instance = pygad.GA(
        keep_elitism=1,
        init_range_low=min_value,
        init_range_high=max_value,
        num_genes=num_genes,
        num_generations=num_generations,
        sol_per_pop=sol_per_pop,
        num_parents_mating=num_parents_mating,
        mutation_num_genes=mutation_num_genes,
        random_mutation_min_val=min_value,
        random_mutation_max_val=max_value,
        fitness_func=fitness_functions["weierstrass_real"],
        parent_selection_type=selection_methods["tournament"],
        crossover_type="uniform",
        mutation_type=mutation_methods["random"],
        K_tournament=3,
        on_generation=on_generation
    )

    ga_instance.run()

    summary(ga_instance)
    create_directories()
    do_plots(num_generations)
