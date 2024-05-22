import pygad


def summary(ga_instance: pygad.GA):
    best = ga_instance.best_solution()
    solution, solution_fitness, solution_idx = best
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=1. / solution_fitness))
    ga_instance.best_solutions_fitness = [1. / x for x in ga_instance.best_solutions_fitness]
    ga_instance.plot_fitness()
