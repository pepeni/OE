import pygad
import numpy as np
import matplotlib.pyplot as plt
import os

fitness_values = []
average_values = []
std_values = []


def on_generation(ga_instance: pygad.GA):
    ga_instance.logger.info("Generation = {generation}".format(generation=ga_instance.generations_completed))
    solution, solution_fitness, solution_idx = ga_instance.best_solution(
        pop_fitness=ga_instance.last_generation_fitness)
    ga_instance.logger.info("Best    = {fitness}".format(fitness=1. / solution_fitness))
    ga_instance.logger.info("Individual    = {solution}".format(solution=repr(solution)))

    tmp = [1. / x for x in ga_instance.last_generation_fitness]
    fitness_values.append(1. / solution_fitness)
    average_values.append(np.average(tmp))
    std_values.append(np.std(tmp))

    ga_instance.logger.info("Min    = {min}".format(min=np.min(tmp)))
    ga_instance.logger.info("Max    = {max}".format(max=np.max(tmp)))
    ga_instance.logger.info("Average    = {average}".format(average=np.average(tmp)))
    ga_instance.logger.info("Std    = {std}".format(std=np.std(tmp)))
    ga_instance.logger.info("\r\n")


def create_directories():
    output_data_path = 'output_data'
    plots_path = os.path.join(output_data_path, 'plots')

    for path in [output_data_path, plots_path]:
        if not os.path.exists(path):
            os.makedirs(path)


def do_plots(iterations: int) -> None:
    plot_iteration_values(iterations)
    plot_average_and_std_deviation(iterations)


def plot_iteration_values(iterations: int) -> None:
    iterations = range(1, len(average_values) + 1)
    plt.plot(iterations, fitness_values, label='Najlepsza wartość funkcji')
    plt.xlabel('Iteracja')
    plt.ylabel('Wartość')
    plt.title('Najlepsza wartość funkcji od kolejnej iteracji')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join("output_data/plots", "best_fitness.png"))
    plt.show()


def plot_average_and_std_deviation(iterations: int) -> None:
    iterations = range(1, len(average_values) + 1)
    plt.plot(iterations, average_values, label='Średnia wartość funkcji')
    plt.fill_between(iterations,
                     np.subtract(average_values, std_values),
                     np.add(average_values, std_values),
                     color='gray', alpha=0.2, label='Odchylenie standardowe')
    plt.xlabel('Iteracja')
    plt.ylabel('Wartość')
    plt.title('Średnia wartość funkcji i odchylenie standardowe od kolejnej iteracji')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join("output_data/plots", "average_std_deviation.png"))
    plt.show()
