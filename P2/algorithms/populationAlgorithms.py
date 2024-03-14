import random
def calculate_step(start, end, num_bits):
    # Todo sprawdzić
    return (end - start) / (2**num_bits - 1)

def generate_population(num_individuals, num_bits):
    population = []
    for _ in range(num_individuals):
        individual = [random.randint(0, 1) for _ in range(num_bits)]
        population.append(individual)
    return population

def calculate_value(start, step, individual):
    value = start
    for bit in individual:
        value += step * bit
    return value

def number_to_individual(number, start, step, num_bits):
    #Todo sprawdzić
    individual = []
    for _ in range(num_bits):
        bit = 0 if number < start else 1
        individual.append(bit)
        number -= step
    return individual