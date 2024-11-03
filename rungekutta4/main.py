import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def g(t, u):
    return t ** 2 - u

def rungekutta(a, b, N, alpha):
    h = (b - a) / N
    t_values = np.linspace(a, b, N + 1)
    w_values = np.zeros(N + 1)

    t_values[0] = a
    w_values[0] = alpha

    for i in range(1, N + 1):
        t = t_values[i - 1]
        w = w_values[i - 1]

        k1 = h * g(t, w)
        k2 = h * g(t + h / 2, w + k1 / 2)
        k3 = h * g(t + h / 2, w + k2 / 2)
        k4 = h * g(t + h, w + k3)

        w_values[i] = w + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t_values[i] = a + i * h

        # Afisam valorile actualizate
        print(f"t:{t_values[i]}, w(t): {w_values[i]}")

    return t_values, w_values

# Parametrii problemei
a = 0
b = 1
N = 10
alpha = 0

# Apelarea metodei Runge-Kutta de ordinul 4
t_values, w_values = rungekutta(a, b, N, alpha)

# Plotarea rezultatelor
plt.figure(figsize=(12, 6))
plt.plot(t_values, w_values, 'o-', label='Numeric (RK4)')
plt.xlabel('t')
plt.ylabel('w(t)')
plt.title('Solutia Numerica folosind RK4')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('runge_kutta_4_plot.png')
print("Graficul solutiei numerice a fost salvat ca 'runge_kutta_4_plot.png'")
