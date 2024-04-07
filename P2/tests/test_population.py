import unittest
from src.population import Population
from src.fitness_function import FitnessFunction


def func_x(values: list[float]):
    return [x**2 for x in values]


class TestPopulation(unittest.TestCase):
    def setUp(self):
        self.population_size = 20
        self.number_of_variables = 3
        self.chromosome_length = 25
        self.min_value = -10
        self.max_value = 10
        self.fitness_function = FitnessFunction(func_x)
        self.epochs = 100
        self.population = Population(self.population_size, self.number_of_variables, self.chromosome_length,
                                     self.min_value, self.max_value, self.fitness_function, self.epochs)

    def test_population_size(self):
        self.assertEqual(len(self.population.individuals), self.population_size)

    def test_individual_chromosomes_length(self):
        for individual in self.population.individuals:
            self.assertEqual(len(individual.chromosomes), self.number_of_variables)

    def test_chromosome_genes_length(self):
        for individual in self.population.individuals:
            for chromosome in individual.chromosomes:
                self.assertEqual(len(chromosome.genes), self.chromosome_length)

    def test_chromosome_genes_range(self):
        for individual in self.population.individuals:
            for chromosome in individual.chromosomes:
                for gene in chromosome.genes:
                    self.assertIn(gene, [0, 1])

    def test_decoded_values_range(self):
        for individual in self.population.individuals:
            for value in individual.decoded_values:
                self.assertGreaterEqual(value, self.min_value)
                self.assertLessEqual(value, self.max_value)

    def test_fitness_evaluation(self):
        for individual in self.population.individuals:
            self.assertEqual(individual.fitness_value, func_x(individual.decoded_values))


if __name__ == '__main__':
    unittest.main()
