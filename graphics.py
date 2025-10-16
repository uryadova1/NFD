import matplotlib.pyplot as plt

def graphics(x, h):
    plt.figure(figsize=(10, 6))
    plt.plot(x, h, 'k o', markersize=0.8)
    plt.xlabel("x")
    plt.ylabel("h(x, t)")
    plt.grid()
    plt.show()

def p_and_h_graphic(xp, p, x, h, T, n):
    plt.figure(figsize=(10, 6))
    plt.plot(x, h, 'k o', markersize=0.8, label=f"T: {T}\nn: {n}")
    plt.plot(xp, p, label=f"p", linestyle="dotted", color="blue")
    plt.xlabel("x")
    plt.ylabel("h(x, t)")
    plt.legend()
    plt.grid()
    plt.show()


def graphics13(results):
    for T, data in results.items():
        plt.figure(figsize=(10, 6))
        for order, (x, h, _) in data.items():
            plt.plot(x, h, label=f"Порядок {order}", linewidth=1.2)
        plt.title(f"h(x, t={T})")
        plt.xlabel("x")
        plt.ylabel("h(x, t)")
        plt.grid(True)
        plt.legend()
        plt.savefig(f'./img/task13/T{T}.png')
        plt.show()

def graphics_relative_errors_and_local_orders(results, mode):
    path = f"./img/mode{mode}"
    for T, data in results.items():
        plt.figure(figsize=(10, 6))
        for order, vals in data.items():
            plt.plot(vals["x"], vals["p"], label=f"Порядок {order}", linewidth=1.2)
        plt.title(f"Локальные порядки t={T}")
        plt.xlabel("x")
        plt.ylabel("p(x)")
        plt.grid(True)
        plt.legend()
        plt.savefig(path + f"/T{T}_relative_orders.png")
        plt.show()

        plt.figure(figsize=(10, 6))
        for order, vals in data.items():
            plt.plot(vals["x"], vals["err"], label=f"Порядок {order}", linewidth=1.2)
        plt.title(f"Относительные ошибки t={T}")
        plt.xlabel("x")
        plt.ylabel("ε(x)")
        # plt.yscale("log")
        plt.grid(True, which="both", linestyle="--", linewidth=0.5)
        plt.legend()
        plt.savefig(path + f"/T{T}_runge_errors.png")
        plt.show()
