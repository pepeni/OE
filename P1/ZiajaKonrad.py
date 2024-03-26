import random
import numpy as np

def dcUniform(parent1, parent2):
    size = min(len(parent1), len(parent2))
    random1 = random.randint(0, size - 1)
    random2 = random.randint(0, size - 1)
    xPoint1, xPoint2 = min(random1, random2), max(random1, random2)
    print(xPoint1, xPoint2)
    print("xPoint1: ", xPoint1, " xPoint2: ", xPoint2)
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


ind1 = np.random.randint(0,2,10)
ind2 = np.random.randint(0,2,10)

print("Rodzic1: ", ind1, "\nRodzic2: ", ind2)
newInd1, newInd2 = dcUniform(ind1, ind2)
print("Dziecko1: ", newInd1, "\nDziecko2: ", newInd2, "\n\n")


ind1 = np.random.randint(0,2,30)
ind2 = np.random.randint(0,2,30)

print("Rodzic1: ", ind1, "\nRodzic2: ", ind2)
newInd1, newInd2 = dcUniform(ind1, ind2)
print("Dziecko1: ", newInd1, "\nDziecko2: ", newInd2)
