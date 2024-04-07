
class Chromosome:
    def __init__(self, length: int, genes: list[int]) -> None:
        self.length = length
        self.genes = genes

    def __str__(self) -> str:
        return str(self.genes)

    def __repr__(self) -> list[int]:
        return self.genes
