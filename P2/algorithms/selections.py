import random

# Jak szukamy mamksimum, to zmienić look_for_max na True
def best_selection(population, fitness_function, num_selected, look_for_max = False):
    fitness_values = [fitness_function(individual) for individual in population]
    sorted_population = [x for _, x in sorted(zip(fitness_values, population), reverse=look_for_max)]
    selected_individuals = sorted_population[:num_selected]
    return selected_individuals

# Jak szukamy mamksimum, to zmienić look_for_max na True
def tournament_selection(population, fitness_function, num_selected, tournament_size=4, look_for_max = False):
    # TODO poprawić, żeby losowało wymaganą ilość
    selected_individuals = []
    while len(selected_individuals) < num_selected:
        # Wybierz losowo osobników na turniej
        tournament = random.sample(population, tournament_size)
        # Oblicz wartość funkcji dla każdego osobnika na turnieju
        tournament_fitness = [fitness_function(individual) for individual in tournament]
        # Wybierz zwycięzcę turnieju (osobnika z najwyższą wartością funkcji)
        if look_for_max:
            winner_index = tournament_fitness.index(max(tournament_fitness))
        else:
            winner_index = tournament_fitness.index(min(tournament_fitness))
        selected_individuals.append(tournament[winner_index])
    return selected_individuals

# Jak szukamy mamksimum, to zmienić look_for_max na True
