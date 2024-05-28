import numpy as np

def dissociated_crossover(parents, offspring_size, ga_instance):
    offspring = []
    idx = 0
    while len(offspring) < offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()
        chromosome_length = parent1.shape[0]
        
        random1 = np.random.randint(0, chromosome_length)
        random2 = np.random.randint(0, chromosome_length)
        cross_point_1, cross_point_2 = min(random1, random2), max(random1, random2)

        child1 = parent1.copy()
        child2 = parent2.copy()
        child1[cross_point_1:cross_point_2] = np.bitwise_or(parent1[cross_point_1:cross_point_2], parent2[cross_point_1:cross_point_2])
        child2[cross_point_1:cross_point_2] = np.bitwise_and(parent1[cross_point_1:cross_point_2], parent2[cross_point_1:cross_point_2])

        offspring.append(child1)
        offspring.append(child2)
        idx += 1

    return np.array(offspring[:offspring_size[0]])


def difference_based_crossover(parents, offspring_size, ga_instance):
    offspring = []
    idx = 0
    while len(offspring) < offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()
        diff_indices = [i for i in range(parent1.shape[0]) if parent1[i] != parent2[i]]
        if len(diff_indices) == 0:
            offspring.append(parent1)
            offspring.append(parent2)
        else:
            cross_point = np.random.choice(diff_indices)
            child1 = parent1.copy()
            child2 = parent2.copy()
            child1[cross_point:], child2[cross_point:] = parent2[cross_point:], parent1[cross_point:]
            offspring.append(child1)
            offspring.append(child2)
        idx += 1

    return np.array(offspring[:offspring_size[0]])
