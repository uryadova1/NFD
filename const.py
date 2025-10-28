from fractions import Fraction
import sympy as sp


def art_vis_coeffs_count(n):
    coefficients = [1]
    current = 1
    for k in range(1, n // 2 + 1):
        current = current * (n - k + 1) // k
        coefficients.append(current)

    return coefficients


def coeffs_count(order: int):
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
        coeffs.append(-1 * Fraction(solution[sp.symbols(f'a{i}')]))

    return coeffs


g = 10
