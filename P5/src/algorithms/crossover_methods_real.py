import numpy as np


def arithmetic_crossover(parents, offspring_size, ga_instance):
    offspring = []
    idx = 0
    while len(offspring) < offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()
        alpha = np.random.random()
        child1 = alpha * parent1 + (1 - alpha) * parent2
        child2 = alpha * parent2 + (1 - alpha) * parent1
        offspring.append(child1)
        offspring.append(child2)
        idx += 1
    return np.array(offspring[:offspring_size[0]])


def linear_crossover(parents, offspring_size, ga_instance):
    offspring = []
    idx = 0
    while len(offspring) < offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()
        geneZ = 0.5 * parent1 + 0.5 * parent2
        geneV = 1.5 * parent2 - 0.5 * parent1
        geneX = -0.5 * parent2 + 1.5 * parent1
        offspring.append(geneZ)
        offspring.append(geneV)
        offspring.append(geneX)
        idx += 1
    return np.array(offspring[:offspring_size[0]])


def mixed_alfa_crossover(parents, offspring_size, ga_instance):
    offspring = []
    idx = 0
    alpha = 0.25
    while len(offspring) < offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()
        delta = np.abs(parent1 - parent2)
        a, b = np.minimum(parent1, parent2), np.maximum(parent1, parent2)
        child1 = np.random.uniform(a - delta * alpha, b + delta * alpha)
        child2 = np.random.uniform(a - delta * alpha, b + delta * alpha)
        offspring.append(child1)
        offspring.append(child2)
        idx += 1
    return np.array(offspring[:offspring_size[0]])


def mixed_alfa_beta_crossover(parents, offspring_size, ga_instance):
    offspring = []
    idx = 0
    alpha = 0.25
    beta = 0.7
    while len(offspring) < offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()
        delta = np.abs(parent1 - parent2)
        a, b = np.minimum(parent1, parent2), np.maximum(parent1, parent2)
        child1 = np.random.uniform(a - delta * alpha, b + delta * beta)
        child2 = np.random.uniform(a - delta * alpha, b + delta * beta)
        offspring.append(child1)
        offspring.append(child2)
        idx += 1
    return np.array(offspring[:offspring_size[0]])


def averaging_crossover(parents, offspring_size, ga_instance):
    offspring = []
    idx = 0
    while len(offspring) < offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()
        child = (parent1 + parent2) / 2
        offspring.append(child)
        offspring.append(child.copy())
        idx += 1
    return np.array(offspring[:offspring_size[0]])


def geometric_crossover(parents, offspring_size, ga_instance):
    offspring = []
    idx = 0
    while len(offspring) < offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()
        child = np.where((parent1 > 0) & (parent2 > 0), np.sqrt(parent1 * parent2), (parent1 + parent2) / 2)
        offspring.append(child)
        offspring.append(child.copy())
        idx += 1
    return np.array(offspring[:offspring_size[0]])


def diverse_crossover(parents, offspring_size, ga_instance):
    offspring = []
    idx = 0
    beta = 0.5
    while len(offspring) < offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()
        random_gene = np.random.randint(1, parent1.shape[0] - 1)
        child1 = np.zeros(parent1.shape)
        child2 = np.zeros(parent2.shape)
        domain_lower, domain_upper = np.min(parent1), np.max(parent1)
        
        child1[:random_gene] = parent1[:random_gene]
        child2[:random_gene] = parent2[:random_gene]

        gene1 = parent1[random_gene] + (parent2[random_gene] - parent1[random_gene]) * beta
        gene2 = domain_lower + beta * (domain_upper - domain_lower)
        child1[random_gene] = gene1
        child2[random_gene] = gene2

        child1[random_gene + 1:] = parent2[random_gene + 1:]
        child2[random_gene + 1:] = parent1[random_gene + 1:]
        
        offspring.append(child1)
        offspring.append(child2)
        idx += 1
    return np.array(offspring[:offspring_size[0]])
