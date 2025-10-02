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