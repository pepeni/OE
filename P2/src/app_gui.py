import time
import tkinter as tk
from tkinter import messagebox

from P2.src.algorithms.crossover_methods import CrossoverMethods
from P2.src.algorithms.fitness_function_methods import FitnessFunctionMethods
from P2.src.algorithms.inversion_methods import InversionMethods
from P2.src.algorithms.mutation_methods import MutationMethods
from P2.src.algorithms.selection_methods import SelectionMethods
from P2.src.entry_with_placeholder import EntryWithPlaceholder
from P2.src.fitness_function import FitnessFunction
from P2.src.population import Population

functionOptions = {
    "Goldstein and Price (2 variables)": FitnessFunctionMethods.goldstein_and_price,
    "Weierstrass (n variables)": FitnessFunctionMethods.weierstrass,
    "Simple func (1 variable)": FitnessFunctionMethods.simple_func
}

selectionOptions = {
    "Best": SelectionMethods.best_selection,
    "Tournament": SelectionMethods.tournament_selection,
    "Roulette": SelectionMethods.roulette_wheel_selection
}

crossOptions = {
    "Single Point": CrossoverMethods.single_point_crossover,
    "Double Point": CrossoverMethods.double_point_crossover,
    "Triple Point": CrossoverMethods.triple_point_crossover,
    "Uniform": CrossoverMethods.uniform_crossover,
    "Discrete": CrossoverMethods.discrete_crossover,
    "Dissociated": CrossoverMethods.dissociated_crossover,
    "Difference based": CrossoverMethods.differences_based_crossover
}

mutationOptions = {
    "Edge": MutationMethods.edge_mutation,
    "Single Point": MutationMethods.single_point_mutation,
    "Double Point": MutationMethods.double_point_mutation
}

inversionOptions = {
    "Simple inversion": InversionMethods.double_point_inversion
}


class AppGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x850")
        self.root.title("P2 OE app")
        self.root.configure(bg="#333333")

        self.createLabel("Obliczenia Ewolucyjne projekt 2", 16)

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

        self.bitNumberEntry = EntryWithPlaceholder(self.root, placeholder="Liczba bitów")
        self.bitNumberEntry.pack(pady=5)

        self.epochNumberEntry = EntryWithPlaceholder(self.root, placeholder="Liczba epok")
        self.epochNumberEntry.pack(pady=5)

        self.selectionPercentEntry = EntryWithPlaceholder(self.root,
                                                          placeholder="Procent osobników z selekcji")
        self.selectionPercentEntry.pack(pady=5)

        self.elitePercentEntry = EntryWithPlaceholder(self.root, placeholder="Procent elite strategy")
        self.elitePercentEntry.pack(pady=5)

        self.xProbabilityEntry = EntryWithPlaceholder(self.root, placeholder="Prawd. krzyżowania")
        self.xProbabilityEntry.pack(pady=5)

        self.mProbabilityEntry = EntryWithPlaceholder(self.root, placeholder="Prawd. mutacji")
        self.mProbabilityEntry.pack(pady=5)

        self.inversionProbabilityEntry = EntryWithPlaceholder(self.root, placeholder="Prawd. inwersji")
        self.inversionProbabilityEntry.pack(pady=5)

        # Dropdown selekcji
        self.createLabel("Metoda selekcji")

        self.selectionVar = tk.StringVar()
        self.selectionVar.set("Best")

        self.selectionDrop = tk.OptionMenu(self.root, self.selectionVar, *selectionOptions.keys())
        self.selectionDrop.pack()
        self.configureDropdownMenu(self.selectionDrop)

        self.createLabel("Metoda krzyżowania")

        self.crossVar = tk.StringVar()
        self.crossVar.set("Single Point")

        self.crossDrop = tk.OptionMenu(self.root, self.crossVar, *crossOptions.keys())
        self.crossDrop.pack()
        self.configureDropdownMenu(self.crossDrop)

        self.createLabel("Metoda mutacji")

        self.mutationVar = tk.StringVar()
        self.mutationVar.set("Edge")

        self.mutationDrop = tk.OptionMenu(self.root, self.mutationVar, *mutationOptions.keys())
        self.mutationDrop.pack()
        self.configureDropdownMenu(self.mutationDrop)

        self.createLabel("Metoda inwersji")

        self.inversionVar = tk.StringVar()
        self.inversionVar.set("Simple inversion")

        self.inversionDrop = tk.OptionMenu(self.root, self.inversionVar, *inversionOptions.keys())
        self.inversionDrop.pack()
        self.configureDropdownMenu(self.inversionDrop)


        button = tk.Button(self.root, text="Wykonaj", font=('Arial', 18), command=self.whenClick, bg="#333333",
                           fg="white")
        button.pack(pady=10)

        self.root.mainloop()

    def whenClick(self):
        placeholders = [
            "Ilosc zmiennych"
            "Punkt startowy - a",
            "Punkt końcowy - b",
            "Wielkosc populacji",
            "Liczba bitów",
            "Liczba epok",
            "Liczba osobników wyłoniona z selekcji turniejowej lub best",
            "Liczba elite strategy",
            "Prawd. krzyżowania",
            "Prawd. mutacji",
            "Prawd. inwersji",
            ""
        ]

        try:
            if self.numberOfVariablesEntry.get() not in placeholders:
                self.numberOfVariables = int(self.numberOfVariablesEntry.get())
            else:
                self.numberOfVariables = 2

            if self.startEntry.get() not in placeholders:
                self.start = int(self.startEntry.get())
            else:
                self.start = 0

            if self.endEntry.get() not in placeholders:
                self.end = int(self.endEntry.get())
            else:
                self.end = 0

            if self.populationNumberEntry.get() not in placeholders:
                self.populationNumber = int(self.populationNumberEntry.get())
            else:
                self.populationNumber = 100

            if self.bitNumberEntry.get() not in placeholders:
                self.bitNumber = int(self.bitNumberEntry.get())
            else:
                self.bitNumber = 10

            if self.epochNumberEntry.get() not in placeholders:
                self.epochNumber = int(self.epochNumberEntry.get())
            else:
                self.epochNumber = 50

            if self.selectionPercentEntry.get() not in placeholders:
                self.selectionPercent = float(self.selectionPercentEntry.get())
            else:
                self.selectionPercent = 0.5

            if self.elitePercentEntry.get() not in placeholders:
                self.elitePercent = float(self.elitePercentEntry.get())
            else:
                self.elitePercent = 0.1

            if self.xProbabilityEntry.get() not in placeholders:
                self.xProbability = float(self.xProbabilityEntry.get())
            else:
                self.xProbability = 0.7

            if self.mProbabilityEntry.get() not in placeholders:
                self.mProbability = float(self.mProbabilityEntry.get())
            else:
                self.mProbability = 0.01

            if self.inversionProbabilityEntry.get() not in placeholders:
                self.inversionProbability = float(self.inversionProbabilityEntry.get())
            else:
                self.inversionProbability = 0.05

            population = Population(size=self.populationNumber, number_of_variables=self.numberOfVariables,
                                    chromosome_length=self.bitNumber,
                                    min_value=self.start, max_value=self.end,
                                    fitness_function=FitnessFunction(functionOptions[self.functionVar.get()]),
                                    epochs=self.epochNumber, selection_percent=self.selectionPercent,
                                    elite_percent=self.elitePercent, crossover_prob=self.xProbability,
                                    mutation_prob=self.mProbability, inversion_prob=self.inversionProbability)
            population.set_selection_method(selectionOptions[self.selectionVar.get()])
            population.set_crossover_method(crossOptions[self.crossVar.get()])
            population.set_mutation_method(mutationOptions[self.mutationVar.get()])
            population.set_inversion_method(inversionOptions[self.inversionVar.get()])

            start_time = time.time()

            population.evolve()

            end_time = time.time()

            self.executionTime = end_time - start_time
            self.solutionFound(population.get_best_individual().fitness_value)

            print("\n\n---Najlepsze osobniki z kazdej epoki---")
            population.print_best_individuals()

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