import random


def edgeM(parent, probability):
    size = len(parent)
    random_var = random.random()
    if random_var < probability:
        if parent[size-1] == 1:
            parent[size-1] = 0
        else:
            parent[size-1] = 1

    return parent

def singlePointM(parent, probability):
    size = len(parent)
    random_var = random.random()
    if random_var < probability:
        index = random.randint(0, size-1)
        if parent[index] == 1:
            parent[index] = 0
        else:
            parent[index] = 1

    return parent

def doublePointM(parent, probability):
    size = len(parent)
    random_var = random.random()
    if random_var < probability:
        index1 = random.randint(0, size-1)
        index2 = random.randint(0, size-1)

        if parent[index1] == 1:
            parent[index1] = 0
        else:
            parent[index1] = 1

        if parent[index2] == 1:
            parent[index2] = 0
        else:
            parent[index2] = 1

    return parent
