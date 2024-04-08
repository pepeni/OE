import statistics
import time
from tqdm import tqdm

from src.algorithms.crossover_methods import CrossoverMethods
from src.algorithms.fitness_function_methods import FitnessFunctionMethods
from src.algorithms.inversion_methods import InversionMethods
from src.algorithms.mutation_methods import MutationMethods
from src.algorithms.selection_methods import SelectionMethods
from src.fitness_function import FitnessFunction
from src.population import Population

if __name__ == '__main__':
    execution_times = []
    results = []
    for i in tqdm(range(100)):
        population = Population(size=50, number_of_variables=2, chromosome_length=10, min_value=-2, max_value=2,
                                fitness_function=FitnessFunction(FitnessFunctionMethods.goldstein_and_price), epochs=100,
                                selection_percent=0.5, elite_percent=0.1,
                                crossover_prob=0.8, mutation_prob=0.1, inversion_prob=0.05)
        population.set_selection_method(SelectionMethods.tournament_selection)
        population.set_crossover_method(CrossoverMethods.differences_based_crossover)
        population.set_mutation_method(MutationMethods.double_point_mutation)
        population.set_inversion_method(InversionMethods.double_point_inversion)
        start_time = time.time()

        population.evolve()
        end_time = time.time()
        execution_time = end_time - start_time

        result = population.get_best_individual().fitness_value
        execution_times.append(execution_time)
        results.append(result)

    print(f'Sredni czss wykonania: {statistics.mean(execution_times)}')
    print(f'Sredni wynik: {statistics.mean(results)}')
