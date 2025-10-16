from const import coeffs
from countData import calculate_p, runge_error
from graphics import graphics13, graphics_relative_errors_and_local_orders
from run import start_NFD
from datetime import datetime


def task13():
    X = 10
    a = 2
    b = 10
    x_start = 0
    x_end = x_start + X

    times = [0.5, 1, 2]
    orders = [4, 6, 8, 10]
    N = 50

    results = dict()

    for T in times:
        results[T] = {}
        for order in orders:
            a_coeffs = coeffs(order)
            x, h, q = start_NFD(x_start, x_end, X, a_coeffs, N, T, a, b)
            results[T][order] = (x, h, order)
    graphics13(results)


def task_relative_errors_and_local_orders():
    X = 10
    a = 2
    b = 10
    x_start = 0
    x_end = x_start + X
    times = [0.5, 1, 2]
    orders = [4, 6, 8, 10]
    N = list()
    mode = int(input("1: сетка 100, 200, 400\n2: сетка 250, 500, 1000\n3: сетка 1000, 2000, 4000\nmode: "))
    if mode == 1:
        N = [100, 200, 400]
    elif mode == 2:
        N = [250, 500, 1000]
    elif mode == 3:
        N = [1000, 2000, 4000]

    results = dict()

    t_start = datetime.now()
    for T in times:
        results[T] = {}
        print(f"T = {T}")
        for order in orders:
            a_coeffs = coeffs(order)
            t1 = datetime.now()
            print(f"start N = {N[0]}")
            x1, h1, q1 = start_NFD(x_start, x_end, X, a_coeffs, N[0], T, a, b)
            t2 = datetime.now()
            print(f"Count NFD on {N[0]}-dot grid is {t2-t1}, order is {order}")

            print(f"start N = {N[1]}")
            t1 = datetime.now()
            x2, h2, q2 = start_NFD(x_start, x_end, X, a_coeffs, N[1], T, a, b)
            t2 = datetime.now()
            print(f"Count NFD on {N[1]}-dot grid is {t2 - t1}, order is {order}")

            print(f"start N = {N[2]}")
            t1 = datetime.now()
            x3, h3, q3 = start_NFD(x_start, x_end, X, a_coeffs, N[2], T, a, b)
            t2 = datetime.now()
            print(f"Count NFD on {N[2]}-dot grid is {t2 - t1}, order is {order}")


            p = calculate_p(h1, h2, h3, q1, q2, q3)
            u2, u1 = q2/h2, q1/h1
            runge_err = runge_error(u1, u2, p)

            # для p и rung_err получается самая маленькая сетка, из за срезов в формулах

            results[T][order] = {
                "x": x1,
                "p": p,
                "err": runge_err
            }
        print()
    t_finish = datetime.now()
    print(f"Total time is {t_finish-t_start}")
    graphics_relative_errors_and_local_orders(results, mode)
