import time

from P4.src.algorithms.crossover_methods import CrossoverMethods
from P4.src.algorithms.fitness_function_methods import FitnessFunctionMethods
from P4.src.algorithms.inversion_methods import InversionMethods
from P4.src.algorithms.mutation_methods import MutationMethods
from P4.src.algorithms.selection_methods import SelectionMethods
from P4.src.fitness_function import FitnessFunction
from P4.src.population import Population

if __name__ == '__main__':
    population = Population(size=50, number_of_variables=2, min_value=-2.0, max_value=2.0,
                            fitness_function=FitnessFunction(FitnessFunctionMethods.goldstein_and_price), epochs=100,
                            selection_percent=0.5, elite_percent=0.1,
                            crossover_prob=0.8, mutation_prob=0.1, inversion_prob=0.05)
    population.set_selection_method(SelectionMethods.best_selection)
    population.set_crossover_method(CrossoverMethods.geometric_crossover)
    population.set_mutation_method(MutationMethods.uniform_mutation)
    population.set_inversion_method(InversionMethods.simple_inversion)

    start_time = time.time()
    population.evolve()
    end_time = time.time()
    execution_time = end_time - start_time

    result = population.get_best_individual().fitness_value

    print(f'Czas wykonania: {execution_time}')
    print(f'Wynik: {result}')
