import os

from mealpy import FloatVar, WarSO
import numpy as np
import time
from opfunu import cec_based
from tqdm import tqdm


def objective_function(solution):
    return np.sum(solution ** 2)


def goldstein_and_price(solution: list[float]) -> float:
    if len(solution) != 2:
        raise AttributeError
    x0, x1 = solution
    term1 = 1.0 + (x0 + x1 + 1.0) ** 2 * (19.0 - 14.0 * x0 + 3.0 * x0 ** 2 - 14.0 * x1 + 6.0 * x0 * x1 + 3.0 * x1 ** 2)
    term2 = 30.0 + (2.0 * x0 - 3.0 * x1) ** 2 * (
                18.0 - 32.0 * x0 + 12.0 * x0 ** 2 + 48.0 * x1 - 36.0 * x0 * x1 + 27.0 * x1 ** 2)
    fitness = term1 * term2
    return fitness


def weierstrass(solution: list[float]) -> float:
    ndim = len(solution)
    if ndim not in [10, 20, 30, 50, 100]:
        raise AttributeError
    func = cec_based.cec2014.F62014(ndim=ndim)
    fitness = func.evaluate(np.array(solution))
    return fitness


def create_directories():
    output_data_path = 'output_data'
    plots_path = os.path.join(output_data_path, 'plots')
    summary_results_path = os.path.join(output_data_path, 'summary_results')

    for path in [output_data_path, plots_path, summary_results_path]:
        if not os.path.exists(path):
            os.makedirs(path)


fitness_functions = {
    "goldstein_and_price_binary": goldstein_and_price,
    "weierstrass_binary": weierstrass
}


if __name__ == "__main__":

    create_directories()

    fitness_function_name = "weierstrass_binary"
    epochs = 150
    pop_size = 50
    rr_values = np.linspace(0.1, 0.9, num=9)

    # floatVar = FloatVar(lb=(-2.,) * 2, ub=(2.,) * 2, name="delta") # goldstein & price
    floatVar = FloatVar(lb=(-100.,) * 10, ub=(100.,) * 10, name="delta") # weierstrass
    problem_dict = {
        "bounds": floatVar,
        "minmax": "min",
        "obj_func": fitness_functions[fitness_function_name],
        "log_to": None
    }

    execution_times = []
    solutions = []
    fitness_results = []

    with open(f'output_data/summary_results/{fitness_function_name}_{epochs}_{pop_size}_WSO.txt', "w") as output_file:
        for rr in tqdm(rr_values):
            rr = float(rr)
            for i in tqdm(range(100)):
                model = WarSO.OriginalWarSO(epoch=epochs, pop_size=pop_size, rr=rr)

                start_time = time.time()
                model.solve(problem_dict)
                end_time = time.time()
                execution_time = end_time - start_time

                solution = model.g_best.solution
                fitness = model.g_best.target.fitness
                execution_times.append(execution_time)
                solutions.append(solution)
                fitness_results.append(fitness)
                execution_times.append(execution_time)

            print(f'rr = {rr}')
            print(f'Sredni czss wykonania: {np.mean(execution_times)}')
            print(f'Sredni wynik: {np.mean(fitness_results)}')
            print('-------------------\n')

            output_file.write(f'rr = {rr}\n')
            output_file.write(f'Sredni czss wykonania: {np.mean(execution_times)}\n')
            output_file.write(f'Sredni wynik: {np.mean(fitness_results)}\n')
            output_file.write(f'-------------------\n')
