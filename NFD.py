import numpy as np
from fractions import Fraction
from const import g


def L(l, a):  # np.array
    l = np.concatenate((l[-3:], l, l[:3]))
    a1, a2, a3 = a
    return -a3 * l[:-6] - a2 * l[1:-5] - a1 * l[2:-4] + a1 * l[4:-2] + a2 * l[5:-1] + a3 * l[6:]


def F(q: np.ndarray, h: np.ndarray):
    return np.array(q ** 2 / h + g * h ** 2 / 2)


def NFD(q_n: np.ndarray, h_n: np.ndarray, a, dt: float):
    # step 1
    l1 = L(h_n, a)
    l_arg_tmp = F(q_n, h_n)
    l2 = L(l_arg_tmp, a)

    h_1 = h_n + dt * l1
    q_1 = q_n + dt * l2  # - правильно ли

    # step 2
    l1 = L(h_1, a)
    l_arg_tmp = F(q_1, h_1)
    l2 = L(l_arg_tmp, a)

    h_2 = (3 * h_n + h_1 + dt * l1) / 4
    q_2 = (3 * q_n + q_1 + dt * l2) / 4

    # step 3
    l1 = L(h_2, a)
    l_arg_tmp = F(q_2, h_2)
    l2 = L(l_arg_tmp, a)

    h_n_plus_1 = (h_n + 2 * h_2 + 2 * dt * l1) / 3
    q_n_plus_1 = (q_n + 2 * q_2 + 2 * dt * l2) / 3

    return h_n_plus_1, q_n_plus_1
