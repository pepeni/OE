import random

def diverse_crossover(parent1, parent2, beta):
    n = len(parent1)
    
    l = random.randint(1, n - 1)
    
    child1 = [0] * n
    child2 = [0] * n

    domain_lower = min(parent1)

    domain_upper = max(parent1)

    for i in range(l):
        child1[i] = parent1[i] 
        child2[i] = parent2[i] 
    
    child1[l] = parent1[l] + (parent2[l] - parent1[l]) * beta
    child2[l] = domain_lower + beta * (domain_upper - domain_lower)

    for i in range(l + 1, n):
        child1[i] = parent2[i] 
        child2[i] = parent1[i] 
    
    return child1, child2

# Przykładowe użycie
parent1 = [1.3, 2.5, 3.7, 4.1]
parent2 = [5.9, 6.7, 7.2, 8.4]
beta = 0.5
child1, child2 = diverse_crossover(parent1, parent2, beta)
print("Rodzic 1:", parent1)
print("Rodzic 2:", parent2)
print("Potomek 1:", child1)
print("Potomek 2:", child2)
