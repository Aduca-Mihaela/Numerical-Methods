import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def g(t, u):
    # Definim functia corespunzatoare ecuatiei diferentiale u' = g(t, u)
    return t ** 2 - u

def runge_kutta_2(a, b, N, alpha):
    h = (b - a) / N
    t_values = np.linspace(a, b, N + 1)
    w_values = np.zeros(N + 1)

    t_values[0] = a
    w_values[0] = alpha

    print(f"({t_values[0]}, {w_values[0]})")

    for i in range(1, N + 1):
        t = t_values[i - 1]
        w = w_values[i - 1]

        k1 = h * g(t, w)
        k2 = h * g(t + h / 2, w + k1 / 2)

        w_values[i] = w + k2
        t_values[i] = a + i * h

        print(f"t = {t_values[i]}, w(t) = {w_values[i]}")

    return t_values, w_values

# Parametrii problemei
a = 0
b = 1
N = 10
alpha = 0

# Apelarea metodei Runge-Kutta de ordinul 2
t_values, w_values = runge_kutta_2(a, b, N, alpha)

# Plotarea rezultatelor
plt.figure(figsize=(12, 6))
plt.plot(t_values, w_values, 'o-', label='Numeric (RK2)')
plt.xlabel('t')
plt.ylabel('w(t)')
plt.title('Solutia Numerica folosind RK2')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('runge_kutta_2_plot.png')
print("Graficul solutiei numerice a fost salvat ca 'runge_kutta_2_plot.png'")