### Funkcje:
- goldstein_and_price - 2 zmienne,  [min, max] - [-2, 2], minima - (3.0, [0.0, -1.0])
- weierstrass - 2 zmienne(mozna tez n zmiennych) [min, max] - [-20, 20] (chyba), minima - ? 

### Przykladowa inicjalizacja Populacji

- population = Population(size=20, number_of_variables=2, chromosome_length=10, min_value=-2, max_value=2,
                            fitness_function=FitnessFunction(FitnessFunctionMethods.goldstein_and_price), epochs=20)
### wybranie metod selekcji, krzyzowania, mutacji
- population.set_selection_method(SelectionMethods.best_selection)
- population.set_crossover_method(CrossoverMethods.differences_based_crossover)
- population.set_mutation_method(MutationMethods.double_point_mutation)

### odpalenie algorytmu:
population.evolve()

### wyswietlanie osobnikow w populacji i najlepszych osobnikow dla kazdej epoki:

- population.print_individuals()
- population.print_best_individuals()


## Przykladowe odpalenie gui
- a: -2
- b: 2
- wielkosc populacji: 20
- liczba bitow: 10
- liczba epok: 50
- procent osobnikow selekcja: 0.5
- procent elite: 0.1
- prawd krzyzowania: 0.8
- prawd mutacji: 0.2
- prawd inwersji: 0.2
- Selekcja: Best
- Krzyzowanie: Difference based
- Mutacja: Double Point

## Link do sprawozdania
- https://docs.google.com/document/d/1qrqLNccACs7av_RQvni-39oxi0MXc2eedHZYH7W2F4g/edit?usp=sharing
