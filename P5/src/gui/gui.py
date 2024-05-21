import time
import tkinter as tk
from tkinter import messagebox
import os

from P4.src.algorithms.fitness_function_methods import FitnessFunctionMethods
from P4.src.gui.entry_with_placeholder import EntryWithPlaceholder

representationOptions = {
    "Binary": "int",
    "Real": "float"
}

functionOptions = {
    "Goldstein and Price (2 variables)": FitnessFunctionMethods.goldstein_and_price,
    "Weierstrass (10, 20, 30, 50, 100)": FitnessFunctionMethods.weierstrass,
}

selectionOptions = {
    "Tournament": "tournament",
    "Roulette": "rws",
    "Random": "random",
}

crossOptions = {
    "Single point": "single_point",
    "Two points": "two_points",
    "Uniform": "uniform",

    # our funcs
    # binary repr
    "Dissociated": "dissociated",
    "Difference based": "difference_based",

    # real repr
    "Arithmetic": "arithmetic_crossover",
    "Linear": "linear_crossover",
    "Mixed alfa": "mixed_alfa_crossover",
    "Mixed alfa & beta": "mixed_alfa_beta_crossover",
    "Averaging": "averaging_crossover",
    "Geometric": "geometric_crossover",
    "Diverse": "diverse_crossover"
}

mutationOptions = {
    "Random": "random",
    "Swap": "swap",

    # our func
    "Gauss": "gauss_mutation"
}


def create_directories():
    output_data_path = 'output_data'
    iterations_path = os.path.join(output_data_path, 'iterations')
    plots_path = os.path.join(output_data_path, 'plots')

    for path in [output_data_path, iterations_path, plots_path]:
        if not os.path.exists(path):
            os.makedirs(path)


class Gui:
    def __init__(self):
        self.executionTime = None
        self.root = tk.Tk()
        self.root.geometry("500x850")
        self.root.title("P5 OE app")
        self.root.configure(bg="#333333")

        self.createLabel("Wybierz reprezentacje")

        self.representationVar = tk.StringVar()
        self.representationVar.set("Real")

        self.representationDrop = tk.OptionMenu(self.root, self.representationVar, *representationOptions.keys())
        self.representationDrop.pack(pady=10)
        self.configureDropdownMenu(self.representationDrop)

        self.createLabel("Testowana funkcja")

        self.functionVar = tk.StringVar()
        self.functionVar.set("Goldstein and Price (2 variables)")

        self.functionDrop = tk.OptionMenu(self.root, self.functionVar, *functionOptions.keys())
        self.functionDrop.pack(pady=10)
        self.configureDropdownMenu(self.functionDrop)

        self.numberOfVariablesEntry = EntryWithPlaceholder(self.root, placeholder="Ilosc zmiennych")
        self.numberOfVariablesEntry.pack(pady=5)

        self.startEntry = EntryWithPlaceholder(self.root, placeholder="Punkt startowy - a")
        self.startEntry.pack(pady=5)

        self.endEntry = EntryWithPlaceholder(self.root, placeholder="Punkt końcowy - b")
        self.endEntry.pack(pady=5)

        self.populationNumberEntry = EntryWithPlaceholder(self.root, placeholder="Wielkosc populacji")
        self.populationNumberEntry.pack(pady=5)

        self.epochNumberEntry = EntryWithPlaceholder(self.root, placeholder="Liczba epok")
        self.epochNumberEntry.pack(pady=5)

        self.selectionPercentEntry = EntryWithPlaceholder(self.root, placeholder="Procent osobników z selekcji")

        self.createLabel("Metoda selekcji")

        self.selectionVar = tk.StringVar()
        self.selectionVar.set("Best")

        self.selectionDrop = tk.OptionMenu(self.root, self.selectionVar, *selectionOptions.keys())
        self.selectionDrop.pack()
        self.configureDropdownMenu(self.selectionDrop)

        self.createLabel("Metoda krzyżowania")

        self.crossVar = tk.StringVar()
        self.crossVar.set("Arithmetic")

        self.crossDrop = tk.OptionMenu(self.root, self.crossVar, *crossOptions.keys())
        self.crossDrop.pack()
        self.configureDropdownMenu(self.crossDrop)

        self.createLabel("Metoda mutacji")

        self.mutationVar = tk.StringVar()
        self.mutationVar.set("Uniform")

        self.mutationDrop = tk.OptionMenu(self.root, self.mutationVar, *mutationOptions.keys())
        self.mutationDrop.pack()
        self.configureDropdownMenu(self.mutationDrop)

        button = tk.Button(self.root, text="Wykonaj", font=('Arial', 18), command=self.whenClick, bg="#333333",
                           fg="white")
        button.pack(pady=10)

        self.root.mainloop()

    def whenClick(self):
        placeholders = [
            "Ilosc zmiennych" # num_genes
            "Punkt startowy - a", # init_range_low
            "Punkt końcowy - b", # init_range_high
            "Wielkosc populacji", # sol_per_pop
            "Liczba epok", # num_generations
            "Procent osobników wyłoniony z selekcji", #num_parents_mating
        ]

        try:
            if self.numberOfVariablesEntry.get() not in placeholders:
                self.numberOfVariables = int(self.numberOfVariablesEntry.get())
            else:
                self.numberOfVariables = 2

            if self.startEntry.get() not in placeholders:
                self.start = float(self.startEntry.get())
            else:
                self.start = 0.0

            if self.endEntry.get() not in placeholders:
                self.end = float(self.endEntry.get())
            else:
                self.end = 0.0

            if self.populationNumberEntry.get() not in placeholders:
                self.populationNumber = int(self.populationNumberEntry.get())
            else:
                self.populationNumber = 100

            if self.epochNumberEntry.get() not in placeholders:
                self.epochNumber = int(self.epochNumberEntry.get())
            else:
                self.epochNumber = 50

            if self.selectionPercentEntry.get() not in placeholders:
                self.selectionPercent = float(self.selectionPercentEntry.get())
            else:
                self.selectionPercent = 0.5

            # population = Population(size=self.populationNumber, number_of_variables=self.numberOfVariables,
            #                         min_value=self.start, max_value=self.end,
            #                         fitness_function=FitnessFunction(functionOptions[self.functionVar.get()]),
            #                         epochs=self.epochNumber, selection_percent=self.selectionPercent,
            #                         elite_percent=self.elitePercent, crossover_prob=self.xProbability,
            #                         mutation_prob=self.mProbability, inversion_prob=self.inversionProbability)
            # population.set_selection_method(selectionOptions[self.selectionVar.get()])
            # population.set_crossover_method(crossOptions[self.crossVar.get()])
            # population.set_mutation_method(mutationOptions[self.mutationVar.get()])
            # population.set_inversion_method(inversionOptions[self.inversionVar.get()])
            #
            # start_time = time.time()
            # population.evolve()
            # end_time = time.time()
            #
            # create_directories()
            # population.save_to_file_every_iteration("output_data/iterations/results.txt")
            # population.plot_iteration_values()
            # population.plot_average_and_std_deviation()
            #
            # self.executionTime = end_time - start_time
            # self.solutionFound(population.get_best_individual().fitness_value)
            #
            # print("\n\n---Najlepsze osobniki z kazdej epoki---")
            # population.print_best_individuals()

        except AttributeError:
            messagebox.showerror("Wrong number of variables", "Change the number of variables with the number corresponding to the function")

        except:
            messagebox.showerror("Incorect Data", "Provided data is in incorrect format")

    def solutionFound(self, result: float):
        messagebox.showinfo("Solution found", f"Result: {result}\nTime: {self.executionTime}")

    def configureDropdownMenu(self, dropdownmenu):
        dropdownmenu.config(bg="#333333", fg="white", font=('Arial', 12), width=25, activebackground="#111111",
                                  activeforeground="white", highlightthickness=0)
        dropdownmenu['menu'].config(
            bg="#333333", fg="white", font=('Arial', 12), activebackground="#111111", activeforeground="white"
        )

    def createLabel(self, text, font = 12):
        label = tk.Label(self.root, text=text, font=('Arial', font), bg="#333333",
                                  fg="white")
        label.pack(pady=5)
