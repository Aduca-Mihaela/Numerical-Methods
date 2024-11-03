import numpy as np
import matplotlib

matplotlib.use('TkAgg')  # Setează backend-ul Matplotlib la TkAgg
import matplotlib.pyplot as plt


# Definirea funcției g(t, w)
def g(t, w):
    return w - t ** 2 + 1  # Exemplu simplu pentru demonstrație


# Metoda Adams-Moulton cu patru pași
def adams_moulton_four(w, t, h):
    N = len(w)
    for i in range(3, N - 1):
        # Estimare inițială pentru w[i+1] folosind metoda explicită Adams-Bashforth
        w_predict = w[i] + h / 24 * (55 * g(t[i], w[i]) -
                                     59 * g(t[i - 1], w[i - 1]) +
                                     37 * g(t[i - 2], w[i - 2]) -
                                     9 * g(t[i - 3], w[i - 3]))

        # Iterații pentru rezolvarea ecuației implicite
        for _ in range(5):  # Puteți ajusta numărul de iterații pentru precizie
            w_predict = w[i] + h / 720 * (251 * g(t[i + 1], w_predict) +
                                          646 * g(t[i], w[i]) -
                                          264 * g(t[i - 1], w[i - 1]) +
                                          106 * g(t[i - 2], w[i - 2]) -
                                          19 * g(t[i - 3], w[i - 3]))

        w[i + 1] = w_predict
    return w


# Parametrii specifici ai problemei
a, b = 0, 2  # Intervalul [a, b]
alpha = 0.5  # Condiția inițială u(a) = alpha
N = 10  # Numărul total de pași
h = (b - a) / N  # Calculul lui h
t_values = np.linspace(a, b, N)
w_values = np.zeros(N)
w_values[0] = alpha  # Inițializează prima valoare

# Inițializare simplă a primelor patru valori folosind Euler sau similar
for i in range(3):
    w_values[i + 1] = w_values[i] + h * g(t_values[i], w_values[i])

# Aplicarea metodei Adams-Moulton cu patru pași
w_values = adams_moulton_four(w_values, t_values, h)

# Afișarea soluțiilor într-un format aliniat
print("{:<10} {:<20}".format('Timp t', 'Soluția w'))
for t, w in zip(t_values, w_values):
    print("{:<10} {:<20}".format(t, w))

# Crearea și afișarea graficului
plt.figure(figsize=(10, 6))
plt.plot(t_values, w_values, label='Adams-Moulton 4 Steps', linestyle='-', marker='o', color='red')
plt.title('Solutia unei ecuatii diferentiale folosind Metoda Adams-Moulton cu 4 pasi')
plt.xlabel('Timpul t')
plt.ylabel('Solutia w')
plt.legend()
plt.grid(True)
plt.show()
