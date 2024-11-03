import matplotlib
matplotlib.use('TkAgg')  # Setează backend-ul Matplotlib la TkAgg

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

def g(t, x):
    return t + x

def successive_approximations(t0, x0, T, N):
    t_values = np.linspace(t0, T, N)  # Valorile lui t la care să evaluăm soluția
    x = np.zeros(N)  # Inițializare vector de soluții
    x[0] = x0  # Condiția inițială

    # Calculul aproximărilor succesive
    for n in range(1, N):
        def integral(s):
            return g(s, x[n - 1])

        # Integrează g(s, x_{n-1}(s)) de la t0 la t_values[n]
        result, _ = quad(integral, t0, t_values[n])

        x[n] = x0 + result

    return t_values, x

t0 = 0  # Timpul inițial
x0 = 1  # Valoarea inițială
T = 2  # Timpul final până la care să evaluăm soluția
N = 50  # Numărul de puncte în discretizare

t_values, x_values = successive_approximations(t0, x0, T, N)


plt.figure(figsize=(10, 6))
plt.plot(t_values, x_values, label='Aproximații succesive', color='darkblue', linestyle='-', linewidth=2, marker='o', markersize=5)
plt.title('Aproximații succesive ale soluției ecuației diferențiale', fontsize=16, fontweight='bold')
plt.xlabel('Timp t', fontsize=14)
plt.ylabel('Soluția x(t)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.show()
