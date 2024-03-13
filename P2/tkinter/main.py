import tkinter as tk
from EntryWithPlaceholder import EntryWithPlaceholder

class App:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("500x800")
        self.root.title("P2 OE app")
        self.root.configure(bg="#333333")

        topLabel = tk.Label(self.root, text="Obliczenia Ewolucyjne projekt 2", font=('Arial', 18), bg="#333333", fg="white")
        topLabel.pack(pady=10)

        startEntry = EntryWithPlaceholder(self.root, placeholder="Punkt startowy - a")
        startEntry.pack(pady=5)

        endEntry = EntryWithPlaceholder(self.root, placeholder="Punkt końcowy - b")
        endEntry.pack(pady=5)

        populationNumberEntry = EntryWithPlaceholder(self.root, placeholder="Liczba populacji")
        populationNumberEntry.pack(pady=5)

        bitNumberEntry = EntryWithPlaceholder(self.root, placeholder="Liczba bitów")
        bitNumberEntry.pack(pady=5)

        epochNumberEntry = EntryWithPlaceholder(self.root, placeholder="Liczba epok")
        epochNumberEntry.pack(pady=5)

        individualsNumberEntry = EntryWithPlaceholder(self.root, placeholder="Liczba osobników wyłoniona z selekcji turniejowej lub best")
        individualsNumberEntry.pack(pady=5)

        eliteStrategyNumber = EntryWithPlaceholder(self.root, placeholder="Liczba elite strategy")
        eliteStrategyNumber.pack(pady=5)

        xProbabilityEntry = EntryWithPlaceholder(self.root, placeholder="Prawd. krzyżowania")
        xProbabilityEntry.pack(pady=5)

        mProbabilityEntry = EntryWithPlaceholder(self.root, placeholder="Prawd. mutacji")
        mProbabilityEntry.pack(pady=5)

        inversionProbabilityEntry = EntryWithPlaceholder(self.root, placeholder="Prawd. inwersji")
        inversionProbabilityEntry.pack(pady=5)


        # Dropdown selekcji
        selectionLabel = tk.Label(self.root, text="Metoda selekcji", font=('Arial', 12), bg="#333333",
                               fg="white")
        selectionLabel.pack(pady=5)

        selectionOptions = [
            "Best",
            "Roulette",
            "Tournament"
        ]

        selectionVar = tk.StringVar()
        selectionVar.set("Best")

        selectionDrop = tk.OptionMenu(self.root, selectionVar, *selectionOptions)
        selectionDrop.pack()
        selectionDrop.config(bg="#333333", fg="white", font=('Arial', 12), width=15)

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

        crossVar = tk.StringVar()
        crossVar.set("Single Point")

        crossDrop = tk.OptionMenu(self.root, crossVar, *crossOptions)
        crossDrop.pack()
        crossDrop.config(bg="#333333", fg="white", font=('Arial', 12), width=15)

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

        mutationVar = tk.StringVar()
        mutationVar.set("Single Point")

        mutationDrop = tk.OptionMenu(self.root, mutationVar, *mutationOptions)
        mutationDrop.pack()
        mutationDrop.config(bg="#333333", fg="white", font=('Arial', 12), width=15)

        param8Label = tk.Label(self.root, text="Maksymalizacja?", font=('Arial', 12), bg="#333333",
                               fg="white")
        param8Label.pack(pady=5)

        def myClick():
            print(startEntry.get())

        button = tk.Button(self.root, text="Wykonaj", font=('Arial', 18), command=self.whenClick)
        button.pack()



        self.root.mainloop()

    def whenClick(self):
        print("done")
        #ToDo



App()