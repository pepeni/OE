import math


class FitnessFunctionMethods:
    @staticmethod
    def simple_func(values: list[float]):
        if len(values) != 1:
            raise AttributeError
        return [x ** 2 + 3 for x in values]

    @staticmethod
    def goldstein_and_price(values: list[float]):
        if len(values) != 2:
            raise AttributeError
        x0, x1 = values
        term1 = 1 + (x0 + x1 + 1) ** 2 * (19 - 14 * x0 + 3 * x0 ** 2 - 14 * x1 + 6 * x0 * x1 + 3 * x1 ** 2)
        term2 = 30 + (2 * x0 - 3 * x1) ** 2 * (18 - 32 * x0 + 12 * x0 ** 2 + 48 * x1 - 36 * x0 * x1 + 27 * x1 ** 2)
        return term1 * term2

    @staticmethod
    def weierstrass(values: list[float]):
        a = 0.5
        b = 3
        kmax = 20
        term1 = 0
        term2 = 0
        for x in values:
            for k in range(kmax + 1):
                term1 += (a ** k) * math.cos(2 * math.pi * (b ** k) * (x + 0.5))
                term2 += (a ** k) * math.cos(2 * math.pi * (b ** k) * 0.5)
        return term1 - term2
