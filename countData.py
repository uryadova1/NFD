import numpy as np


def calculate_p(h1, h2, h3, q1, q2, q3):
    h1 = np.asarray(h1, dtype=float)
    h2 = np.asarray(h2, dtype=float)[::2]
    h3 = np.asarray(h3, dtype=float)[::4]
    q1 = np.asarray(q1, dtype=float)
    q2 = np.asarray(q2, dtype=float)[::2]
    q3 = np.asarray(q3, dtype=float)[::4]

    norm1 = ((h1 - h2) ** 2 + (q1 - q2) ** 2) ** (1 / 2)
    norm2 = ((h2 - h3) ** 2 + (q2 - q3) ** 2) ** (1 / 2)

    try:
        # gg = abs(norm1 / norm2)
        # - пришлось эту муть развести, потому что питон упорно не соглашался, что к типу np.ndarray применим логарифм.....
        # gg = np.array(gg)
        p = np.log(np.array(abs(norm1 / norm2))) / np.log(2)
        return p
    except TypeError:
        print("omg type error (opat'........)")


def runge_error(u_h, u_h2, p):
    error = abs(np.linalg.norm(u_h2[::2] - u_h, ord=2) / (2 ** p - 1))
    return error
