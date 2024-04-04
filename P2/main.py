from src.app_gui import AppGui
from src.fitness_function import FitnessFunction
from src.population import Population


def func_x(values: list[float]):
    return [x**2 for x in values]


if __name__ == '__main__':
    AppGui()

    # population = Population(10, 2, 10, -10, 10, FitnessFunction(func_x))
    # for ind in population.individuals:
    #     print(ind.__repr__(), ind.decoded_values, ind.fitness_value)
