import copy
import random

from P2.src.individual import Individual
from P2.src.population import get_sorted_individuals


class SelectionMethods:
    @staticmethod
    def best_selection(individuals: list[Individual], number_to_select: int, look_for_max=False) -> list[Individual]:
        sorted_population = get_sorted_individuals(individuals, look_for_max)
        selected_individuals = sorted_population[:number_to_select]
        return selected_individuals

    @staticmethod
    def tournament_selection(individuals: list[Individual], number_to_select: int, look_for_max=False) -> list[Individual]:
        winners = []
        candidates = copy.deepcopy(individuals)
        while len(winners) < number_to_select:
            tournament_candidates = []
            for _ in range(2):
                candidate = random.choice(candidates)
                tournament_candidates.append(candidate)
            if look_for_max:
                winner = max(tournament_candidates, key=lambda x: x.fitness_value)
                candidates.remove(winner)
            else:
                winner = min(tournament_candidates, key=lambda x: x.fitness_value)
                candidates.remove(winner)
            winners.append(winner)
        return winners

    @staticmethod
    def roulette_wheel_selection(individuals: list[Individual], number_to_select: int, look_for_max=False) -> list[Individual]:
        if not look_for_max:
            fitness_values = [1 / individual.fitness_value for individual in individuals]
        else:
            fitness_values = [individual.fitness_value for individual in individuals]

        selected_individuals = []
        total_fitness = sum(fitness_values)
        probabilities = [fitness_value / total_fitness for fitness_value in fitness_values]

        while len(selected_individuals) < number_to_select:
            index = random.choices(range(len(individuals)), probabilities)[0]
            selected_individuals.append(individuals[index])

        return selected_individuals
