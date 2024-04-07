import tkinter as tk
from tkinter import messagebox

from src.algorithms.crossover_methods import CrossoverMethods
from src.algorithms.fitness_function_methods import FitnessFunctionMethods
from src.algorithms.mutation_methods import MutationMethods
from src.algorithms.selection_methods import SelectionMethods
from src.entry_with_placeholder import EntryWithPlaceholder
from src.fitness_function import FitnessFunction
from src.population import Population

functionOptions = {
    "Funkcja 1 (2 zmienne)": FitnessFunctionMethods.goldstein_and_price,
    "Funkcja 2 (n zmiennych)": FitnessFunctionMethods.weierstrass
}

selectionOptions = {
    "Best": SelectionMethods.best_selection,
    # "Roulette": SelectionMethods.tournament_selection,
    # "Tournament": SelectionMethods.oulette_wheel_selection
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


class AppGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x800")
        self.root.title("P2 OE app")
        self.root.configure(bg="#333333")

        self.topLabel = tk.Label(self.root, text="Obliczenia Ewolucyjne projekt 2", font=('Arial', 18), bg="#333333",
                                 fg="white")
        self.topLabel.pack(pady=10)

        functionLabel = tk.Label(self.root, text="Testowana funkcja", font=('Arial', 12), bg="#333333",
                                 fg="white")
        functionLabel.pack(pady=5)

        self.functionVar = tk.StringVar()
        self.functionVar.set("Funkcja 1 (2 zmienne)")

        self.functionDrop = tk.OptionMenu(self.root, self.functionVar, *functionOptions.keys())
        self.functionDrop.pack(pady=10)
        self.functionDrop.config(bg="#333333", fg="white", font=('Arial', 12), width=30)

        self.startEntry = EntryWithPlaceholder(self.root, placeholder="Punkt startowy - a")
        self.startEntry.pack(pady=5)

        self.endEntry = EntryWithPlaceholder(self.root, placeholder="Punkt końcowy - b")
        self.endEntry.pack(pady=5)

        self.populationNumberEntry = EntryWithPlaceholder(self.root, placeholder="Liczba populacji")
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
        selectionLabel = tk.Label(self.root, text="Metoda selekcji", font=('Arial', 12), bg="#333333",
                                  fg="white")
        selectionLabel.pack(pady=5)

        self.selectionVar = tk.StringVar()
        self.selectionVar.set("Best")

        self.selectionDrop = tk.OptionMenu(self.root, self.selectionVar, *selectionOptions.keys())
        self.selectionDrop.pack()
        self.selectionDrop.config(bg="#333333", fg="white", font=('Arial', 12), width=15)

        crossLabel = tk.Label(self.root, text="Metoda krzyżowania", font=('Arial', 12), bg="#333333",
                              fg="white")
        crossLabel.pack(pady=5)

        self.crossVar = tk.StringVar()
        self.crossVar.set("Single Point")

        self.crossDrop = tk.OptionMenu(self.root, self.crossVar, *crossOptions.keys())
        self.crossDrop.pack()
        self.crossDrop.config(bg="#333333", fg="white", font=('Arial', 12), width=15)

        mutationLabel = tk.Label(self.root, text="Metoda mutacji", font=('Arial', 12), bg="#333333",
                                 fg="white")
        mutationLabel.pack(pady=5)

        self.mutationVar = tk.StringVar()
        self.mutationVar.set("Edge")

        self.mutationDrop = tk.OptionMenu(self.root, self.mutationVar, *mutationOptions.keys())
        self.mutationDrop.pack()
        self.mutationDrop.config(bg="#333333", fg="white", font=('Arial', 12), width=15)

        param8Label = tk.Label(self.root, text="Maksymalizacja?", font=('Arial', 12), bg="#333333",
                               fg="white")
        param8Label.pack(pady=5)

        button = tk.Button(self.root, text="Wykonaj", font=('Arial', 18), command=self.whenClick, bg="#333333",
                           fg="white")
        button.pack()

        self.root.mainloop()

    def whenClick(self):
        placeholders = [
            "Punkt startowy - a",
            "Punkt końcowy - b",
            "Liczba populacji",
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
            if self.startEntry.get() not in placeholders:
                self.start = float(self.startEntry.get())
            else:
                self.start = 0

            if self.endEntry.get() not in placeholders:
                self.end = float(self.endEntry.get())
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
                self.inversionProbability = 0.0

            population = Population(size=self.populationNumber, number_of_variables=2, chromosome_length=self.bitNumber,
                                    min_value=self.start, max_value=self.end,
                                    fitness_function=FitnessFunction(functionOptions[self.functionVar.get()]),
                                    epochs=self.epochNumber, selection_percent=self.selectionPercent,
                                    elite_percent=self.elitePercent, crossover_prob=self.xProbability,
                                    mutation_prob=self.mProbability, inverse_prob=self.inversionProbability)
            population.set_selection_method(selectionOptions[self.selectionVar.get()])
            population.set_crossover_method(crossOptions[self.crossVar.get()])
            population.set_mutation_method(mutationOptions[self.mutationVar.get()])

            print("--- Prezentacja populacji poczatkowej ---")
            population.print_individuals()

            population.evolve()

            print("\n\n--- Prezentacja populacji koncowej ---")
            population.print_individuals()

            print("\n\n---Najlepsze osobniki z kazdej epoki---")
            population.print_best_individuals()

        except:
            messagebox.showerror("Incorect Data", "provided data is in incorrect format")

    def solutionFound(self):
        # TODO wyświetlić wiadomość z wynikiem, na koniec działania alorytmu
        messagebox.showinfo("solution found")
