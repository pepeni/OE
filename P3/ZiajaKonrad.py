import random


def onePointAverageX(parent1, parent2):
    child1 = []
    child2 = []
    cp = random.randint(0, len(parent1)-1)
    for i in range(len(parent1)):
        child1.append(parent1[i])
        child2.append(parent2[i])
    child1[cp] = (parent1[cp] + parent2[cp]) / 2
    child2[cp] = (parent1[cp] + parent2[cp]) / 2
    return child1, child2

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

print(onePointAverageX(a,b))


