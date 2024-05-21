from opfunu import cec_based
import numpy as np


class FitnessFunctionMethods:
    @staticmethod
    def goldstein_and_price(ga_instance, solution, solution_idx) -> float:
        pass
        # if len(values) != 2:
        #     raise AttributeError
        # x0, x1 = values
        # term1 = 1.0 + (x0 + x1 + 1.0) ** 2 * (19.0 - 14.0 * x0 + 3.0 * x0 ** 2 - 14.0 * x1 + 6.0 * x0 * x1 + 3.0 * x1 ** 2)
        # term2 = 30.0 + (2.0 * x0 - 3.0 * x1) ** 2 * (18.0 - 32.0 * x0 + 12.0 * x0 ** 2 + 48.0 * x1 - 36.0 * x0 * x1 + 27.0 * x1 ** 2)
        # return term1 * term2

    @staticmethod
    def weierstrass(ga_instance, solution, solution_idx) -> float:
        pass
        # if ndim not in [10, 20, 30, 50, 100]:
        #     raise AttributeError
        # func = cec_based.cec2014.F62014(ndim=ndim)
        # return func.evaluate(np.array(values))
