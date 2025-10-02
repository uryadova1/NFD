import numpy as np
from NFD import NFD
from const import g
from countData import calculate_p
from graphics import graphics, p_and_h_graphic


def periodicalU(a: float, x0: np.ndarray, X: float):
    return a * np.sin(2 * np.pi * x0 / X + np.pi / 4)


def periodicalH(b: int, u: np.ndarray):
    return (u + b) ** 2 / (4 * g)


def deltaT(u: np.ndarray, h: np.ndarray, delta_x: float):
    z = 0.5
    c = g * h
    a = max(abs(u) + c)

    return z * delta_x / a


def start_NFD(x_start, x_end, X, n, T, a, b):
    x0 = np.linspace(x_start, x_end, n)
    u0 = periodicalU(a, x0, X)
    h0 = periodicalH(b, u0)
    q0 = h0 * u0
    h_n, q_n, u_n = h0.copy(), q0.copy(), u0.copy()

    delta_x = X / n
    delta_t = deltaT(u0, h0, delta_x)

    time_steps = int(T / delta_t)

    for i in range(time_steps):
        h_n, q_n = NFD(q_n, h_n, delta_t)
    return x0, h_n, q_n


def periodicalProblem(T: float, n: int):
    X = 10
    a = 2
    b = 10
    x_start = 0
    x_end = x_start + X

    x1, h1, q1 = start_NFD(x_start, x_end, X, n, T, a, b)
    x2, h2, q2 = start_NFD(x_start, x_end, X, 2 * n, T, a, b)
    x3, h3, q3 = start_NFD(x_start, x_end, X, 4 * n, T, a, b)

    p = calculate_p(h1, h2, h3, q1, q2, q3)

    # graphics(x3, h3)
    # p_and_h_graphic(x1, p, h1)