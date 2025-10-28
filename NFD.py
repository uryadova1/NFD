import numpy as np
from const import g


def L(l, a_coeffs):
    new_l = np.zeros_like(l)
    a_len = len(a_coeffs)
    l = np.concatenate((l[-a_len - 1: -1], l, l[1: a_len + 1]))
    a_len *= 2

    for i, a in enumerate(a_coeffs[::-1]):
        if i == 0:
            new_l = (-a * l[: -a_len] + a * l[a_len:])
        else:
            new_l = new_l + (-a * l[i: -a_len + i] + a * l[a_len - i: -i])
    return new_l


def artificial_viscosity(vector_old, art_vis, art_vis_coeffs, order):
    length = order // 2
    vector_old = np.concatenate((vector_old[-length - 1: -1], vector_old, vector_old[1: length + 1]))

    new_vec = vector_old[:-order] + vector_old[order:]
    for i, a in enumerate(art_vis_coeffs):
        if i == 0:
            new_vec = vector_old[:-order] + vector_old[order:]
        elif i == length:
            new_vec = new_vec + ((-1) ** i) * a * vector_old[i: -order + i]
        else:
            new_vec = new_vec + ((-1) ** i) * a * (vector_old[i: -order + i] + vector_old[order - i: -i])
    return new_vec / art_vis

    # vector_old = np.concatenate((vector_old[-4:-1], vector_old, vector_old[1:4]))
    # gg2 = ((vector_old[:-6] + vector_old[6:]) - 6 * (vector_old[1:-5] + vector_old[5:-1]) + 15 * (
    #         vector_old[2:-4] + vector_old[4:-2]) - 20 * vector_old[3:-3]) / art_vis


def F(q, h):
    return np.array(q ** 2 / h + g * h ** 2 / 2)


def NFD(q_n, h_n, dt_dx, a_coeffs, art_vis_coeffs, order):
    # step 1
    l1 = L(q_n, a_coeffs)
    l_arg_tmp = F(q_n, h_n)
    l2 = L(l_arg_tmp, a_coeffs)

    h_1 = h_n + dt_dx * l1
    q_1 = q_n + dt_dx * l2

    # step 2
    l1 = L(q_1, a_coeffs)
    l_arg_tmp = F(q_1, h_1)
    l2 = L(l_arg_tmp, a_coeffs)

    h_2 = (3 * h_n + h_1 + dt_dx * l1) / 4
    q_2 = (3 * q_n + q_1 + dt_dx * l2) / 4

    # step 3
    l1 = L(q_2, a_coeffs)
    l_arg_tmp = F(q_2, h_2)
    l2 = L(l_arg_tmp, a_coeffs)

    h_a = artificial_viscosity(h_n, 2 ** order, art_vis_coeffs, order)
    q_a = artificial_viscosity(q_n, 2 ** order, art_vis_coeffs, order)

    h_n_plus_1 = (h_n + 2 * h_2 + 2 * dt_dx * l1) / 3 + h_a
    q_n_plus_1 = (q_n + 2 * q_2 + 2 * dt_dx * l2) / 3 + q_a

    return h_n_plus_1, q_n_plus_1
