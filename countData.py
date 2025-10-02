import numpy as np

def calculate_p(h1, h2, h3, q1, q2, q3):

    h2 = np.array(h2[::2])
    h3 = np.array(h3[::4])

    q2 = np.array(q2[::2])
    q3 = np.array(q3[::4])

    norm1 = ((h1 - h2) ** 2 + (q1 - q2) ** 2) ** (1 / 2)
    norm2 = ((h2 - h3) ** 2 + (q2 - q3) ** 2) ** (1 / 2)
    gg = abs(norm1 / norm2)
    p = np.log2(gg)
    # p = np.log(norm1/norm2)/np.log(2)
    return p


def runge_error(u_h, u_h2, p):
    error = np.linalg.norm(u_h2[::2] - u_h, ord=2) / (2 ** p - 1)
    return error