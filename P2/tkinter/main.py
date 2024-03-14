import tkinter as tk
from EntryWithPlaceholder import EntryWithPlaceholder
from tkinter import messagebox

class App:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("500x800")
        self.root.title("P2 OE app")
        self.root.configure(bg="#333333")

        self.topLabel = tk.Label(self.root, text="Obliczenia Ewolucyjne projekt 2", font=('Arial', 18), bg="#333333", fg="white")
        self.topLabel.pack(pady=10)

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

        self.individualsNumberEntry = EntryWithPlaceholder(self.root, placeholder="Liczba osobników wyłoniona z selekcji turniejowej lub best")
        self.individualsNumberEntry.pack(pady=5)

        self.eliteStrategyNumber = EntryWithPlaceholder(self.root, placeholder="Liczba elite strategy")
        self.eliteStrategyNumber.pack(pady=5)

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

        selectionOptions = [
            "Best",
            "Roulette",
            "Tournament"
        ]

        self.selectionVar = tk.StringVar()
        self.selectionVar.set("Best")

        self.selectionDrop = tk.OptionMenu(self.root, self.selectionVar, *selectionOptions)
        self.selectionDrop.pack()
        self.selectionDrop.config(bg="#333333", fg="white", font=('Arial', 12), width=15)

        crossLabel = tk.Label(self.root, text="Metoda krzyżowania", font=('Arial', 12), bg="#333333",
                               fg="white")
        crossLabel.pack(pady=5)

        crossOptions = [
            "Single Point",
            "Double Point",
            "Triple Point",
            "Uniform",
            "Discrete",
            "Dissociated"
        ]

        self.crossVar = tk.StringVar()
        self.crossVar.set("Single Point")

        self.crossDrop = tk.OptionMenu(self.root, self.crossVar, *crossOptions)
        self.crossDrop.pack()
        self.crossDrop.config(bg="#333333", fg="white", font=('Arial', 12), width=15)

        mutationLabel = tk.Label(self.root, text="Metoda mutacji", font=('Arial', 12), bg="#333333",
                               fg="white")
        mutationLabel.pack(pady=5)

        mutationOptions = [
            "Single Point",
            "Double Point",
            "Triple Point",
            "Uniform",
            "Discrete",
            "Dissociated"
        ]

        self.mutationVar = tk.StringVar()
        self.mutationVar.set("Single Point")

        self.mutationDrop = tk.OptionMenu(self.root, self.mutationVar, *mutationOptions)
        self.mutationDrop.pack()
        self.mutationDrop.config(bg="#333333", fg="white", font=('Arial', 12), width=15)

        param8Label = tk.Label(self.root, text="Maksymalizacja?", font=('Arial', 12), bg="#333333",
                               fg="white")
        param8Label.pack(pady=5)

        button = tk.Button(self.root, text="Wykonaj", font=('Arial', 18), command=self.whenClick, bg="#333333", fg="white")
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
                # Domyślna wartość dla pola start
                self.start = 0.0

            if self.endEntry.get() not in placeholders:
                self.end = float(self.endEntry.get())
            else:
                # Domyślna wartość dla pola end
                self.end = 0.0

            if self.populationNumberEntry.get() not in placeholders:
                self.populationNumber = int(self.populationNumberEntry.get())
            else:
                # Domyślna wartość dla liczby populacji
                self.populationNumber = 100

            if self.bitNumberEntry.get() not in placeholders:
                self.bitNumber = int(self.bitNumberEntry.get())
            else:
                # Domyślna wartość dla liczby bitów
                self.bitNumber = 10

            if self.epochNumberEntry.get() not in placeholders:
                self.epochNumber = int(self.epochNumberEntry.get())
            else:
                # Domyślna wartość dla liczby epok
                self.epochNumber = 50

            if self.individualsNumberEntry.get() not in placeholders:
                self.individualsNumber = int(self.individualsNumberEntry.get())
            else:
                # Domyślna wartość dla liczby osobników
                self.individualsNumber = 50

            if self.eliteStrategyNumber.get() not in placeholders:
                self.eliteNumber = int(self.eliteStrategyNumber.get())
            else:
                # Domyślna wartość dla liczby strategii elitarnych
                self.eliteNumber = 2

            if self.xProbabilityEntry.get() not in placeholders:
                self.xProbability = float(self.xProbabilityEntry.get())
            else:
                # Domyślna wartość dla prawdopodobieństwa krzyżowania
                self.xProbability = 0.7

            if self.mProbabilityEntry.get() not in placeholders:
                self.mProbability = float(self.mProbabilityEntry.get())
            else:
                # Domyślna wartość dla prawdopodobieństwa mutacji
                self.mProbability = 0.01

            if self.inversionProbabilityEntry.get() not in placeholders:
                self.inversionProbability = float(self.inversionProbabilityEntry.get())
            else:
                # Domyślna wartość dla prawdopodobieństwa inwersji
                self.inversionProbability = 0.0
            self.selectionMethod = self.selectionVar.get()
            self.crossMethod = self.crossVar.get()
            self.muationMethod = self.mutationVar.get()

            # ToDo na podstawie informacji zbudować algorytm i go uruchomić

        except:
            messagebox.showerror("Incorect Data", "provided data is in incorrect format")

    def solutionFound(self):
        # TODO wyświetlić wiadomość z wynikiem, na koniec działania alorytmu
        messagebox.showinfo("solution found")

App()