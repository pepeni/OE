import random
import numpy as np


def dissociatedX(parent1, parent2):
    size = min(len(parent1), len(parent2))
    random1 = random.randint(0, size-1)
    random2 = random.randint(0, size-1)
    xPoint1, xPoint2 = min(random1, random2), max(random1, random2)
    child1 = []
    child2 = []
    for i in range(size):
        if i <= xPoint1:
            child1.append(parent1[i])
            child2.append(parent2[i])
        elif xPoint1 < i <= xPoint2:
            child1.append(parent1[i] | parent2[i])
            # nowsza wersja
            child2.append(parent1[i] & parent2[i])
        else:
            child1.append(parent2[i])
            child2.append(parent1[i])

    return np.array(child1), np.array(child2)

def singlePointX(parent1, parent2):
    size = min(len(parent1), len(parent2))
    random1 = random.randint(0, size - 1)
    xPoint1 = random1
    child1 = []
    child2 = []
    for i in range(size):
        if i <= xPoint1:
            child1.append(parent1[i])
            child2.append(parent2[i])
        else:
            child1.append(parent2[i])
            child2.append(parent1[i])

    return np.array(child1), np.array(child2)

def doublePointX(parent1, parent2):
    size = min(len(parent1), len(parent2))
    random1 = random.randint(0, size-1)
    random2 = random.randint(random1, size-1)
    xPoint1, xPoint2 = min(random1, random2), max(random1, random2)
    child1 = []
    child2 = []
    for i in range(size):
        if xPoint1 < i <= xPoint2:
            child1.append(parent2[i])
            child2.append(parent1[i])
        else:
            child1.append(parent1[i])
            child2.append(parent2[i])

    return np.array(child1), np.array(child2)

def triplePointX(parent1, parent2):
    size = min(len(parent1), len(parent2))
    random1 = random.randint(0, size-1)
    random2 = random.randint(0, size-1)
    random3 = random.randint(0, size - 1)
    random_list = [random1, random2, random3]
    random_list.sort()
    xPoint1, xPoint2, xPoint3 = random_list[0], random_list[1], random_list[2]
    child1 = []
    child2 = []
    for i in range(size):
        if xPoint1 < i <= xPoint2 or i > xPoint3:
            child1.append(parent2[i])
            child2.append(parent1[i])
        else:
            child1.append(parent1[i])
            child2.append(parent2[i])

    return np.array(child1), np.array(child2)

def uniformX(parent1, parent2, probability):
    size = min(len(parent1), len(parent2))
    child1 = []
    child2 = []
    for i in range(size):
        random_var = random.random()
        if random_var < probability:
            child1.append(parent2[i])
            child2.append(parent1[i])
        else:
            child1.append(parent1[i])
            child2.append(parent2[i])

    return np.array(child1), np.array(child2)

def discreteX(parent1, parent2):
    size = min(len(parent1), len(parent2))
    child1 = []
    child2 = []
    for i in range(size):
        random_var = random.random()
        if random_var > 0.5:
            child1.append(parent2[i])
            child2.append(parent1[i])
        else:
            child1.append(parent1[i])
            child2.append(parent2[i])

    return np.array(child1), np.array(child2)