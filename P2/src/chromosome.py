from random import randint


class Chromosome:
    def __init__(self, length: int):
        self.length = length
        self.genes = [randint(0, 1) for _ in range(length)]

    def __str__(self):
        return str(self.genes)

    def __repr__(self):
        return self.genes
