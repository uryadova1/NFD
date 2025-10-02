import matplotlib.pyplot as plt

def graphics(x, h):
    plt.figure(figsize=(10, 6))
    plt.plot(x, h, 'k o', markersize=0.8)
    plt.xlabel("x")
    plt.ylabel("h(x, t)")
    plt.grid()
    plt.show()

def p_and_h_graphic(x, h, p):
    plt.figure(figsize=(10, 6))
    plt.plot(x, h, 'k o', markersize=0.8)
    plt.plot(x, p, 'k o', markersize=0.8)
    plt.xlabel("x")
    plt.ylabel("h(x, t)")
    plt.grid()
    plt.show()