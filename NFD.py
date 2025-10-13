import numpy as np
from const import g, a_coeffs


def L(l):  # np.array
    new_l = np.zeros_like(l)
    a_len = len(a_coeffs)
    l = np.concatenate((l[-a_len:], l, l[:a_len]))
    a_len *= 2

    for i, a in enumerate(a_coeffs[::-1]):
        if i == 0:
            new_l = (-a * l[: -a_len + i] + a * l[a_len - i:])
        else:
            new_l = new_l + (-a * l[i: -a_len + i] + a * l[a_len - i: -i])

    # a1, a2, a3 = a_coeffs
    # tmp = -a3 * l[:-6] - a2 * l[1:-5] - a1 * l[2:-4] + a1 * l[4:-2] + a2 * l[5:-1] + a3 * l[6:]
    return new_l


def F(q: np.ndarray, h: np.ndarray):
    return np.array(q ** 2 / h + g * h ** 2 / 2)


def NFD(q_n: np.ndarray, h_n: np.ndarray, dt: float):
    # step 1
    l1 = L(h_n)
    l_arg_tmp = F(q_n, h_n)
    l2 = L(l_arg_tmp)

    h_1 = h_n + dt * l1
    q_1 = q_n + dt * l2  # - правильно ли

    # step 2
    l1 = L(h_1)
    l_arg_tmp = F(q_1, h_1)
    l2 = L(l_arg_tmp)

    h_2 = (3 * h_n + h_1 + dt * l1) / 4
    q_2 = (3 * q_n + q_1 + dt * l2) / 4

    # step 3
    l1 = L(h_2)
    l_arg_tmp = F(q_2, h_2)
    l2 = L(l_arg_tmp)

    h_n_plus_1 = (h_n + 2 * h_2 + 2 * dt * l1) / 3
    q_n_plus_1 = (q_n + 2 * q_2 + 2 * dt * l2) / 3

    return h_n_plus_1, q_n_plus_1
