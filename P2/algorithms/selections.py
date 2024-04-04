import random

# Jak szukamy mamksimum, to zmienić look_for_max na True
def best_selection(population, fitness_function, num_selected, look_for_max = False):
    fitness_values = [fitness_function(individual) for individual in population]
    sorted_population = [x for _, x in sorted(zip(fitness_values, population), reverse=look_for_max)]
    selected_individuals = sorted_population[:num_selected]
    return selected_individuals

# Jak szukamy mamksimum, to zmienić look_for_max na True
def tournament_selection(population, fitness_function, tournament_size=3, look_for_max=False):
    # TODO poprawić, żeby losowało wymaganą ilość o ile potrzebne? Aktualnie zmniejsza populację o 1/3 (+1 jeśli jest reszta)
    winners = []
    population_copy = list(population)
    while population_copy:
        tournament_individuals = random.sample(population_copy, min(tournament_size, len(population_copy)))
        winner = max(tournament_individuals, key=fitness_function) if look_for_max else min(tournament_individuals, key=fitness_function)
        winners.append(winner)
        for i in tournament_individuals:
            population_copy.remove(i)
    return winners


def roulette_wheel_selection(population, fitness_function, look_for_max=False):
    # TODO jak na razie funkcja wybiera tylko jednego osobnika
    if look_for_max == False:
        fitness_values = [1/fitness_function(individual) for individual in population]
    else:
        fitness_values = [fitness_function(individual) for individual in population]

    total_probability = sum(fitness_values)
    probabilities = [p / total_probability for p in fitness_values]

    roulette_wheel = []
    cumulative_sum = 0
    for p in probabilities:
        cumulative_sum += p
        roulette_wheel.append(cumulative_sum)

    random_number = random.random()

    for i, segment in enumerate(roulette_wheel):
        if random_number < segment:
            return population[i]

    return population[-1]