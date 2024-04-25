import benchmark_functions as bf
from opfunu import cec_based
import numpy as np

if __name__ == '__main__':
    func = bf.GoldsteinAndPrice()
    print(f'Przedzial dla pierwszej funkcji: {func.suggested_bounds()}')
    print(f'Miminum funkcj(2 zmienne): {func.minimum()}')

    func2 = cec_based.cec2014.F62014(ndim=10)
    print(f'\nPrzedzial dla drugiej funkcji: {func2.bounds}')
    print(f'Minimum x(10 zmiennych): {func2.x_global}')
    print(f'Minimum - f: {func2.f_global}')
    print(func2.evaluate(np.array([14, 6, 59, -36, -29, -60, 70, 22, -3, 23])))
