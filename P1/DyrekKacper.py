import numpy as np

def create_population(population_size, chromosome_length):
    population = np.random.randint(2, size=(population_size, chromosome_length))
    print("Utworzono populację o rozmiarze:", population_size)
    print("Długość chromosomu:", chromosome_length)
    print("Populacja początkowa:")
    print(population)
    return population

def fitness(chromosome):
    score = np.sum(chromosome)
    print("Funkcja przystosowania dla chromosomu:", score)
    return score

def diagonal_crossover(parents):
    k = len(parents)
    offspring = []

    for i in range(k):
        child = np.zeros_like(parents[0])
        for j in range(len(parents[0])):
            segment = parents[(i + j) % k][j]
            child[j] = segment
        offspring.append(child)
    
    print("Wykonano diagonalne krzyżowanie dla rodziców:")
    for parent in parents:
        print(parent)
    print("Otrzymane potomstwo:")
    for child in offspring:
        print(child)
    
    return offspring

def genetic_algorithm(population_size, chromosome_length, generations):
    population = create_population(population_size, chromosome_length)
    
    for generation in range(generations):
        print("Generacja:", generation + 1)
        
        fitness_values = np.array([fitness(chromosome) for chromosome in population])
        
        selected_indices = np.random.choice(range(population_size), size=population_size, replace=True, p=fitness_values/fitness_values.sum())
        selected_population = population[selected_indices]
        
        new_population = []
        for i in range(0, population_size, 2):
            parents = selected_population[i:i+2]
            children = diagonal_crossover(parents)
            new_population.extend(children)
        
        population = np.array(new_population)
        
    best_individual_index = np.argmax([fitness(chromosome) for chromosome in population])
    best_individual = population[best_individual_index]
    best_fitness = fitness(best_individual)
    
    print("Najlepszy osobnik:", best_individual)
    print("Wartość funkcji przystosowania:", best_fitness)
    
    return best_individual, best_fitness

np.random.seed(0)
population_size = 10
chromosome_length = 8
generations = 5

best_individual, best_fitness = genetic_algorithm(population_size, chromosome_length, generations)
