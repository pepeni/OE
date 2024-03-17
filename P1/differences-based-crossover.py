import numpy as np


def differences_based_crossover(parent1, parent2):
    diff_indices = np.where(ind1 != ind2)[0]
    
    if len(diff_indices) == 0:
        return parent1, parent2
    
    crossover_point = np.random.choice(diff_indices)
    
    child1 = np.copy(parent1)
    child2 = np.copy(parent2)
    
    for i in diff_indices:
        if i >= crossover_point:
            child1[i] = parent2[i]
            child2[i] = parent1[i]
    
    return child1, child2


if __name__ == "__main__":
    ind1 = np.random.randint(0,2,10)
    ind2 = np.random.randint(0,2,10)

    newInd1, newInd2 = differences_based_crossover(ind1, ind2)
    print(f'parent1: {ind1}')
    print(f'parent1: {ind2}')
    print(f'child1: {newInd1}')
    print(f'child1: {newInd2}')
