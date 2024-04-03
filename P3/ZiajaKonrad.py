import random
import math


# Wersja 1
def geometric_crossover(parent1, parent2):
    child = []
    for i in range(len(parent1)):
        if parent1[i] > 0 and parent2[i] > 0:
            child.append(math.sqrt(parent1[i] * parent2[i]))
        else:
            child.append(( parent1[i] + parent2[i] )/ 2)
    return child


parent1 = [1, 2, 3, -4, 5]
parent2 = [6, 7, 8, 9, 10]

child = geometric_crossover(parent1, parent2)
print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Child:", child)
