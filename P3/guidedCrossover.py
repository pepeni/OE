import numpy as np

def create_population(population_size, chromosome_length):
    population = np.random.randint(2, size=(population_size, chromosome_length))
    return population

def fitness(chromosome):
    score = np.sum(chromosome)
    return score

def mutual_fitness(A, B):
    fitness_diff = (fitness(A) - fitness(B)) ** 2
    euclidean_dist = np.linalg.norm(A - B) ** 2
    return fitness_diff / euclidean_dist

def guided_crossover(population, x):
    candidate1_idx = np.random.choice(len(population)) 
    candidate1 = population[candidate1_idx]

    mutual_fitness_values = [mutual_fitness(X, candidate1) for X in population if not np.array_equal(X, candidate1)]
    candidate2_idx = np.argmax(mutual_fitness_values)
    candidate2 = population[candidate2_idx]

    if fitness(candidate2) > fitness(candidate1):
        candidate1, candidate2 = candidate2, candidate1

    L = np.random.uniform(1 - 0.2 * x, 1 + x) 
    result = L * candidate1 + (1 - L) * candidate2

    return result

def genetic_algorithm(population_size, chromosome_length, generations):
    population = create_population(population_size, chromosome_length)
    max_iterations = generations

    for generation in range(generations):
        x = 0.75 * (max_iterations - generation) / max_iterations + 0.25

        offspring = guided_crossover(population, x)
        population = np.vstack((population, offspring))

        population = population[:population_size]

        print("Generacja:", generation + 1)
        for i, chromosome in enumerate(population):
            print("Osobnik", i + 1, ":", chromosome, "Przystosowanie:", fitness(chromosome))

    best_individual_index = np.argmax([fitness(chromosome) for chromosome in population])
    best_individual = population[best_individual_index]
    best_fitness = fitness(best_individual)

    return best_individual, best_fitness

np.random.seed(0)
population_size = 10
chromosome_length = 8
generations = 5

best_individual, best_fitness = genetic_algorithm(population_size, chromosome_length, generations)
print("Najlepszy osobnik:", best_individual)
print("Wartość funkcji przystosowania:", best_fitness)

def run_test(population_size, chromosome_length, generations):
    np.random.seed(0)
    print("Parametry wejściowe:")
    print("Rozmiar populacji:", population_size)
    print("Długość chromosomu:", chromosome_length)
    print("Liczba generacji:", generations)
    best_individual, best_fitness = genetic_algorithm(population_size, chromosome_length, generations)
    print("Najlepszy osobnik:", best_individual)
    print("Wartość funkcji przystosowania:", best_fitness)
    print()

def perform_tests():
    # Test 1
    print("Test 1:")
    run_test(population_size=10, chromosome_length=8, generations=5)

    # Test 2
    print("Test 2:")
    run_test(population_size=20, chromosome_length=10, generations=10)

    # Test 3
    print("Test 3:")
    run_test(population_size=15, chromosome_length=5, generations=7)

    # Test 4
    print("Dodatkowy test:")
    run_test(population_size=12, chromosome_length=6, generations=8)

# Wywołanie funkcji przeprowadzającej testy
perform_tests()
