from fractions import Fraction
import sympy as sp

def coeffs(order: int):
    s = order // 2

    symbols = sp.symbols(f'a1:{s + 1}')
    equations = [sum((j * symbols[j - 1] for j in range(1, s + 1))) - sp.Rational(1, 2)]
    M = list(range(3, order, 2))

    for r in M:
        equation = 0
        for j, a in enumerate(symbols, 1):
            equation += a * (j ** r)
        equations.append(equation)
    solution = sp.solve(equations, symbols)

    coeffs = []
    for i in range(1, s + 1):
        coeffs.append(Fraction(solution[sp.symbols(f'a{i}')]))

    return coeffs


def coeffsCount(order: int):
    return coeffs(order)

g = 10
# order = 8
# a_coeffs = coeffs(order)