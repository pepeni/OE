import numpy as np


def gauss_mutation(offspring, ga_instance):
    probability = ga_instance.mutation_probability
    min_value, max_value = ga_instance.gene_space

    for individual in offspring:
        for i in range(len(individual)):
            if np.random.random() < probability:
                norm_sample = np.random.normal(0, 1)
                new_gene = individual[i] + norm_sample
                
                while new_gene < min_value or new_gene > max_value:
                    norm_sample = np.random.normal(0, 1)
                    new_gene = individual[i] + norm_sample
                
                individual[i] = new_gene
    return offspring
