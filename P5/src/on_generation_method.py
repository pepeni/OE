import pygad
import numpy as np


def on_generation(ga_instance: pygad.GA):
    ga_instance.logger.info("Generation = {generation}".format(generation=ga_instance.generations_completed))
    solution, solution_fitness, solution_idx = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)
    ga_instance.logger.info("Best    = {fitness}".format(fitness=1./solution_fitness))
    ga_instance.logger.info("Individual    = {solution}".format(solution=repr(solution)))

    tmp = [1./x for x in ga_instance.last_generation_fitness]

    ga_instance.logger.info("Min    = {min}".format(min=np.min(tmp)))
    ga_instance.logger.info("Max    = {max}".format(max=np.max(tmp)))
    ga_instance.logger.info("Average    = {average}".format(average=np.average(tmp)))
    ga_instance.logger.info("Std    = {std}".format(std=np.std(tmp)))
    ga_instance.logger.info("\r\n")
