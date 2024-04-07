import random

from src.individual import Individual
from src.population import get_sorted_individuals


class SelectionMethods:
    @staticmethod
    def best_selection(individuals: list[Individual], number_to_select: int, look_for_max=False) -> list[Individual]:
        sorted_population = get_sorted_individuals(individuals, look_for_max)
        selected_individuals = sorted_population[:number_to_select]
        return selected_individuals

    # @staticmethod
    # def tournament_selection(population, fitness_function, tournament_size=3, look_for_max=False):
    #     # TODO poprawić, żeby losowało wymaganą ilość o ile potrzebne? Aktualnie zmniejsza populację o 1/3 (+1 jeśli jest reszta)
    #     winners = []
    #     population_copy = list(population)
    #     while population_copy:
    #         tournament_individuals = random.sample(population_copy, min(tournament_size, len(population_copy)))
    #         winner = max(tournament_individuals, key=fitness_function) if look_for_max else min(tournament_individuals, key=fitness_function)
    #         winners.append(winner)
    #         for i in tournament_individuals:
    #             population_copy.remove(i)
    #     return winners
    #
    # @staticmethod
    # def roulette_wheel_selection(population, fitness_function, look_for_max=False):
    #     # todo jak na razie funkcja wybiera tylko jednego osobnika
    #     if look_for_max == False:
    #         fitness_values = [1/fitness_function(individual) for individual in population]
    #     else:
    #         fitness_values = [fitness_function(individual) for individual in population]
    #
    #     total_probability = sum(fitness_values)
    #     probabilities = [p / total_probability for p in fitness_values]
    #
    #     roulette_wheel = []
    #     cumulative_sum = 0
    #     for p in probabilities:
    #         cumulative_sum += p
    #         roulette_wheel.append(cumulative_sum)
    #
    #     random_number = random.random()
    #
    #     for i, segment in enumerate(roulette_wheel):
    #         if random_number < segment:
    #             return population[i]
    #
    #     return population[-1]