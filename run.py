import numpy as np
from NFD import NFD
from const import g, coeffs
from graphics import graphics


def periodicalU(a: float, x0: np.ndarray, X: float):
    return a * np.sin(2 * np.pi * x0 / X + np.pi / 4)


def periodicalH(b: int, u: np.ndarray):
    return (u + b) ** 2 / (4 * g)


def deltaT(u: np.ndarray, h: np.ndarray, delta_x: float):
    z = 0.5
    c = g * h
    a = max(abs(u) + c)

    return z * delta_x / a


def periodicalProblemConditions(T: float, n: int):
    X = 10
    a = 2
    b = 10
    x_start = 0
    x_end = x_start + X

    a_coeffs = coeffs(6)

    # n = int(input())
    x0 = np.linspace(x_start, x_end, n)
    u0 = periodicalU(a, x0, X)
    h0 = periodicalH(b, u0)
    q0 = h0 * u0
    h_n, q_n, u_n = h0.copy(), q0.copy(), u0.copy()

    delta_x = X / n
    delta_t = deltaT(u0, h0, delta_x)

    time_steps = int(T / delta_t)

    for i in range(time_steps):
        h_n, q_n = NFD(q_n, h_n, a_coeffs, delta_t)

    graphics(x0, h_n)
