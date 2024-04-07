from src.algorithms.crossover_methods import CrossoverMethods
from src.algorithms.fitness_function_methods import FitnessFunctionMethods
from src.algorithms.mutation_methods import MutationMethods
from src.algorithms.selection_methods import SelectionMethods
from src.app_gui import AppGui
from src.fitness_function import FitnessFunction
from src.population import Population

if __name__ == '__main__':
    AppGui()


    # population = Population(size=20, number_of_variables=2, chromosome_length=10, min_value=-2, max_value=2,
    #                         fitness_function=FitnessFunction(FitnessFunctionMethods.goldstein_and_price), epochs=50)
    # population.set_selection_method(SelectionMethods.best_selection)
    # population.set_crossover_method(CrossoverMethods.differences_based_crossover)
    # population.set_mutation_method(MutationMethods.double_point_mutation)
    #
    # print("--- Prezentacja populacji poczatkowej ---")
    # population.print_individuals()
    #
    # population.evolve()
    #
    # print("\n\n--- Prezentacja populacji koncowej ---")
    # population.print_individuals()
    #
    # print("\n\n---Najlepsze osobniki z kazdej epoki---")
    # population.print_best_individuals()
