from turtle import pd

import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Setează backend-ul Matplotlib la TkAgg

import matplotlib.pyplot as plt

# Definirea funcției g(t, w)
def g(t, w):
    return w - t ** 2 + 1


def adams_bashforth_four(w, t, h):
    N = len(w)
    for i in range(3, N - 1):
        w[i + 1] = (w[i] + h / 24 * (55 * g(t[i], w[i]) -
                                     59 * g(t[i - 1], w[i - 1]) +
                                     37 * g(t[i - 2], w[i - 2]) -
                                     9 * g(t[i - 3], w[i - 3])))
    return w


# Parametrii specifici ai problemei
a, b = 0, 2
alpha = 0.5
N = 10  # Numărul total de pași
h = (b - a) / N
t_values = np.linspace(a, b, N)
w_values = np.zeros(N)
w_values[0] = alpha

# Initializare simpla a primelor patru valori folosind Euler
for i in range(3):
    w_values[i + 1] = w_values[i] + h * g(t_values[i], w_values[i])

w_values = adams_bashforth_four(w_values, t_values, h)

print("{:<10} {:<20}".format('Timp t', 'Soluția w'))
for t, w in zip(t_values, w_values):
    print("{:<10} {:<20}".format(t, w))

plt.figure(figsize=(10, 6))
plt.plot(t_values, w_values, label='Adams-Bashforth 4 Steps', linestyle='-', marker='o', color='blue')
plt.title('Solutia unei ecuatii diferentiale folosind Metoda Adams-Bashforth cu 4 pasi')
plt.xlabel('Timpul t')
plt.ylabel('Solutia w')
plt.legend()
plt.grid(True)
plt.show()

