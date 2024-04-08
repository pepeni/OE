import random

def krzyżowanieRównomierne(ind1, ind2, alfa = 0.5):
        size = min(len(ind1), len(ind2))
        for i in range(size):
            if random.random() < alfa:
                print(i)
                ind1[i], ind2[i] = ind2[i], ind1[i]

        return ind1, ind2

def krzyżowanieDwupunktowe(A, B):
    n = min(len(A), len(B))
    cp1 = random.randint(1, n-1)
    cp2 = random.randint(cp1+1, n-1)
    print("1 punkt przcięcia", cp1)
    print("2 punkt przecięcia", cp2)

    C = [0] * n
    D = [0] * n

    
    # Kopia pierwszej części rodziców
    for i in range(0, cp1+1):
        C[i] = A[i]
        D[i] = B[i]
    
    # Zamiana genów między punktami krzyżowania
    for i in range(cp1+1, cp2+1):
        C[i] = B[i]
        D[i] = A[i]
    
    # Kopia drugiej części rodziców
    for i in range(cp2+1, n):
        C[i] = A[i]
        D[i] = B[i]
    
    return C, D

"""
    Funkcja realizująca opisany algorytm krzyżowania w oparciu o 1-bitowe 
    adaptacyjne krzyżowanie (1-Bit Adaptation Crossover).
    
    Parametry:
        - parent1: Pierwszy rodzic (binarna lista/bitowa reprezentacja)
        - parent2: Drugi rodzic (binarna lista/bitowa reprezentacja)
    
    Zwraca:
        - children: Para potomków wygenerowanych po zastosowaniu krzyżowania
    """

def oneBitAdaptationCrossover(parent1, parent2):
    a = parent1[-1]
    b = parent2[-1]

    if a == b == 1:
        return krzyżowanieDwupunktowe(parent1, parent2)
    elif a == b == 0:
        return krzyżowanieRównomierne(parent1, parent2)
    else:
        u = random.random()
        if u < 0.5:
            return krzyżowanieRównomierne(parent1, parent2)
        else:
            return krzyżowanieDwupunktowe(parent1, parent2)

# Funkcja do tworzenia losowej populacji binarnej
def create_population(pop_size, chromosome_length):
    population = []
    for _ in range(pop_size):
        chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
        population.append(chromosome)
    return population

# Funkcja do wyboru dwóch rodziców do krzyżowania
def select_parents(population):
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    return parent1, parent2

def main():
    # Przykładowe użycie
    population_size = 10
    chromosome_length = 8

    population = create_population(population_size, chromosome_length)
    parent1, parent2 = select_parents(population)

    print("Rodzic 1:", parent1)
    print("Rodzic 2:", parent2)
    print(oneBitAdaptationCrossover(parent1, parent2))


